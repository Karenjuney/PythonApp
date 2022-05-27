
import java.util.Scanner;

//psvm+tab 
//sout+tab
public class HolaMundo2 {

    public static void main(String[] args) {
        System.out.println("Hola mundo desde java");

        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Una vez que declaramos la variable con int ya no es necesario volverlo a reiterar y ponemos solo el nombre
        //El metodo main tiene reestricciones y no se podra usar fuera de este metodo. A esto se lo llama el alcance de una 
        //variable
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);

        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
        //crol+click izquierdo nos lleva a donde fue instanciada la variable.
        //Esto quiere decir que el compilador esta reconociendo donde se esta
        //definiendo la variable 

        //Var=inferencia de tipo de datos 
        var miVariableEntera2 = 10;
        //El uso de var nos va a simplificar la definificion de variable
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableCadena2=" + miVariableCadena2);
        //A esto se lo llama concatenacion de cadenas
        //soutv+tab
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //Reglas para definir una variable en Java
        var usuario = "Osvaldo";
        var titulo = "ingeniero";
        var union = titulo + " " + usuario; //Entre las comillas esta el espacio 
        System.out.println("union = " + union);

        var a = 8;
        var b = 11;
        System.out.println(a + b);
        //Si agregamos usuario+a+b se hace una concatenacion y la prioridad es de izq a derecha
        //Si ponemos entre parentesis la suma, recien ahi se puede sumar como corresponde sino se lee como cadena

        //Caracteres especiales en Java
        var nombre = "Natalia";
        System.out.println("Nueva linea: \n" + nombre);//Se hizo un salto de linea
        System.out.println("Tabulador:\t" + nombre);//Un espacio para centrar
        System.out.println("\t.:MENU:.");//Se puede usar varias veces para correrlo mas al centro
        System.out.println("Retroceso:\b" + nombre);//Caracter de retroceso-Osea que va un lugar hacia atras.Borra espacio
        //o borra letras a medida que retrocede
        System.out.println("comillas simple:\'" + nombre + "\'");//Solo son comillas
        System.out.println("Comillas doble:\"" + nombre + "\"");

        //Clase Scanner
        Scanner entrada = new Scanner(System.in);//Aca aprete ctrl+espacio despues de poner NEW y las primeras opciones
        //Hemos creado un objeto de la clase Scanner llamado entrada
        //Es necesario importar esta clase ya que se encuentra definida en otra parte de la clase en JAVA
        //Las clases en java la vamos a empaquetar en Fundas. Esta clase esta dentro de un paquete llamado Java.util. Scanner
        System.out.println("Digite su nombre:");//Este metodo va a leer una linea completa de la consola-La rta se asigna a usuario
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);//Entrada va a ser una variable que iniciamos desde la clase Scanner
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: " + titulo2 + " " + usuario2);
    }
}
