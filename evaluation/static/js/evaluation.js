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