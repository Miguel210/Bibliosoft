var cont = 0;

function register(){

     cont++;
		
		if(cont==1){
		 	$('.box').animate({height:'695px'}, 550);
			$('.show').css('display','block');
			$('#logintoregister').text('Registrate aqui');
			$('#buttonlogintoregister').text('Registrate aqui');
			$('#plogintoregister').text("¿Ya estás registrado?");
			$('#textchange').text('Acceder');
		}
		else
		{
			$('.show').css('display','none');
			$('.box').animate({height:'365px'}, 550);
			$('#logintoregister').text('Login');
			$('#buttonlogintoregister').text('Login');
			$('#plogintoregister').text("No estas registrado?");
			$('#textchange').text('Regístrate');
			cont = 0;
		}
}