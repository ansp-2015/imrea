/*
Ativa a seleção de todos os inputs NT, desabilita os input sem o atributo imrea-nt
*/
var activate_NT = function() {
    link = $('input[imrea-nt="true"]');
    link.each(function(index, element) {
       var v = $(element).val();
       if (v < -100) {
    	   // ativando o elemento
           $(element).addClass('active');
           
           // acionando o radio button
           if ($(element).is(':radio')) {
        	   $(element).prop( "checked", true );
           }
           
           // ativando o label
           var $myLabel = $('label[for="'+ this.id +'"]');
           if ($myLabel.length) {
               $myLabel.addClass('active');
           }
       } else {
           var $myLabel = $('label[for="'+ this.id +'"]');
           $myLabel.addClass('disabled');
       }
    });
}

var deactivate_NT = function() {
    link = $('input[imrea-nt="true"]');
    link.each(function(index, element) {
       var v = $(element).val();
       if (v < -100) {
           $(element).removeClass('active');
           
       } else {
           var $myLabel = $('label[for="'+ this.id +'"]');
           $myLabel.removeClass('disabled');
       }
    });
}

$(document).ready(function() {
	if ( $( "#patient_can_answer__div" ).length ) {
		$("#patient_can_answer_yes").on("click", deactivate_NT);
		$("#patient_can_answer_no").on("click", activate_NT);
	}
});

/*
 * Controle de seleção de pacientes da home page
 */
var evaluation_home_patients_select_change = function() {
  $.get( "ajax_home_patient_periods", { p:this.value } )
      .done(function( data ) {
          var html_content = '';
          for (i = 0; i < data.evaluated_periods.length; i++) {
              period = data.evaluated_periods[i];
              html_content += "<a href='#' data-period-id='"+period.id+"' class='home_period_link list-group-item'><span>"+period.period+"</span>";
              html_content += "<span class='badge'>" + period.qty_evaluated + " / " + period.qty_total_evaluation + "</span>";
              html_content += "</a>";
          }
          $("#home-panel-period-evaluated").html("<div class='list-group'>" + html_content + "</div>");

          html_content = '';
          for (i = 0; i < data.not_evaluated_periods.length; i++) {
              period = data.not_evaluated_periods[i];
              html_content += "<a href='#' data-period-id='"+period.id+"' class='home_period_link list-group-item'>"+period.period+"</a>";
          }
          $("#home-panel-period-not-evaluated").html("<div class='list-group'>" + html_content + "</div>");

          $('.home_period_link').on("click", evaluation_home_period_click);
  });
  if (this.value > 0) {
    $('#home-panel-period').show();
  } else {
    $('#home-panel-period').hide();
  }
}

/**
 * Evento click no nome do período de avaliação de um paciente, na home.
 * Executa um AJAX para buscar as avaliações já respondidas e sem respostas do paciente.
 */
var evaluation_home_period_click = function() {
  $.get( "ajax_home_patient_evaluations",
         { p:$('#evaluation_home_patients_select option:selected').val(),
           period:$(this).attr('data-period-id') } )
      .done(function( data ) {
          if (data.evaluated.length > 0) {
              html_content = '';
                  for (i = 0; i < data.evaluated.length; i++) {
                  obj = data.evaluated[i];
                  html_content += "<a href='" + obj.url +
                                  "' class='home_period_link list-group-item'>" + obj.label + "</a>";
              }
              $("#home-panel-evaluation-evaluated-body").html("<div class='list-group'>" + html_content + "</div>");
              $('#home-panel-evaluation-evaluated-panel').show();
          } else {
//              $('#home-panel-evaluation-evaluated-panel').hide();
              $("#home-panel-evaluation-evaluated-body").html('')
          }

          if (data.not_evaluated.length > 0) {
              html_content = ''
              for (i = 0; i < data.not_evaluated.length; i++) {
                  obj = data.not_evaluated[i];
                  html_content += "<a href='" + obj.url +
                                  "' class='home_period_link list-group-item'>" + obj.label + "</a>";
              }
              $("#home-panel-evaluation-not-evaluated-body").html("<div class='list-group'>" + html_content + "</div>");
              $('#home-panel-evaluation-not-evaluated-panel').show();
          } else {
//              $('#home-panel-evaluation-not-evaluated-panel').hide();
              $("#home-panel-evaluation-not-evaluated-body").html('')
          }
      });
  $('#home-panel-evaluation').show();
}

$(document).ready(function() {
    $('#evaluation_home_patients_select').on("change",evaluation_home_patients_select_change);
    $('#home-panel-period').hide();
    $('#home-panel-evaluation').hide();
});


/**
    Forms: Prepara os eventos para os campos que precisam ser somados no campo de total
    Deve receber o nome que foi declarado no arquivo de Admin do Model.
     addend_field_ids: campos que são as parcelas da soma
     totoal_field._id: campo que receberá o total
*/
var setup_calc_total_field = function(addend_fields, total_field, extra_calc) {
    if (addend_fields && addend_fields.length > 0 && total_field) {
        // preparing the event triggers
        for (var x = 0; x < addend_fields.length; x++) {
            if ($('[name=' + addend_fields[x] + ']').is(':radio')) {
                radios = $('input[type=radio][name=' + addend_fields[x] + ']');
                for (var y = 0; y < radios.length; y++) {
                    $(radios[y]).change(function(){
                        calc_total_field(addend_fields, total_field);
                    });
                }
            } else {
                $('#id_' + addend_fields[x]).change(function(){
                    calc_total_field(addend_fields, total_field);
                    if (extra_calc) {
                        extra_calc();
                    }
                });
            }
        }
        // making the first calculation
        calc_total_field(addend_fields, total_field);
    }
}

/**
    Forms: Executa a soma dos campos.
    Deve receber o nome que foi declarado no arquivo de Admin do Model
     addend_field_ids: campos que são as parcelas da soma
     totoal_field._id: campo que receberá o total
*/
var calc_total_field = function(addend_field_ids, total_field_id) {

    var total_field = $('#id_' + total_field_id);
    // reseting total field value
    total_field.val(0);
    for (var x = 0; x < addend_field_ids.length; x++) {
        // searching radio selected value
        if ($('[name=' + addend_field_ids[x] + ']').is(':radio')){
            // it is a radio but with no selected value
            if(typeof($('[name=' + addend_field_ids[x] + ']:checked').val())!=='undefined') {
                total_field.val(parseInt($('input[type=radio][name=' + addend_field_ids[x] + ']:checked').val()) + parseInt(total_field.val()));
            }
        } else {
            total_field.val((parseInt($('#id_' + addend_field_ids[x]).val()) || 0) + (parseInt(total_field.val()) || 0));
        }
        total_field.trigger("change");
    }
}
