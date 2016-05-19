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
        	   console.log('is radio');
           }
           
           // ativando o label
           var $myLabel = $('label[for="'+ this.id +'"]');
           if ($myLabel.length) {
               $myLabel.addClass('active');
           }
       } else {
           var $myLabel = $('label[for="'+ this.id +'"]');
           console.log($myLabel);
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
              html_content += "<a href='#' data-period-id='"+period.id+"' class='home_period_link list-group-item'>"+period.period+"</a>";
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
                  console.log(obj.url);
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
                  console.log(obj.url);
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
