
function calcular(){

numero1=document.getElementById("n1")[0].value;
numero2=document.getElementById("n2")[0].value;

if(numero1 > numero2)
	{
        //imprime numero mayor
	msgBox("El numero mayor es: " + numero1 + " ( Numero 1 )");
	}
	else
	{
       //imprime numero mayor
       msgBox("El Numero mayor es : " + numero2 + " ( Numero 2 )");
	}

}