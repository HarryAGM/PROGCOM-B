//Comentar solo una linea de código
/*
public: Todo el mundo tiene acceso
class: Es una clase
Nombre del programa
static: Qué es estático. Que no cambia
viod: No retorna nada
Java es un lenguaje de programación fuertemente tipado
*/
public class Main {
//Método constructor
public static void main(String[] args) {
System.out.println("Hola Mundo");
//Tipos de Datos
//Declarando variables
int edad=19;//edad es una variable de tipo entero
double altura=1.73;//altura es una variable de tipo flotante
boolean mayor_edad=true;
String nombre="Hames";
final String MAIL="hgutierrez390@unab.edu.co";
System.out.println(MAIL);
//MAIL="harryagm778@gmail.com";
var apellido="Escorcia";
System.out.println("Tu nombre es: "+nombre+" "+apellido);
System.out.println(apellido);
//EJERCICIOS JAVA
// 1. Crear una variable tipo String nombre y almacenar sus nombres
String NOMBRE = "Harry";
// 2. Crear una variable tipo String apellido y poner sus apellidos
String APELLIDO = "Gutierrez";
// 3. Crear una variable tipo char y almacenar la primera letra de su nombre
char inicial = nombre.charAt(0);
// 4. Imprimir Mi nombre es nombre, apellido
System.out.println("Mi nombre es "+ nombre +", "+ apellido);

// 5. Crear una variable tipo int edad y almacenar la edad
int EDAD = 19;
// 6. Crear una variable tipo flotante y almacenar la estatura
float estatura = 1.73f;
// 7. Imprimir Tengo edad años y mido estatura metros.
System.out.println("Tengo " + edad + " años y mido " + estatura + " metros.");
// 8. Crear una variable tipo booleano que almacene si eres o no mayor de
edad
boolean esMayorDeEdad = edad >= 18;
// 9. Si la variable=true que imprima que eres mayor de edad, de lo contrario,
que eres menor de edad
if (esMayorDeEdad) {
System.out.println("Eres mayor de edad");
} else {
System.out.println("Eres menor de edad");
}
// 10. Imprimir "Eso es todo amigos"
System.out.println("Eso es todo amigos");
}
}
