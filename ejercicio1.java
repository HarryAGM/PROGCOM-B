import java.util.Scanner;
public class ejercicio1 {
    public static void main(String[] args) {
        int Numero;
        Scanner input = new Scanner(System.in);
        System.out.print("Ingresa un número: ");
        Numero = input.nextInt();

        if(Numero > 0){
            System.out.println("El numero es mayor!");
        }
        else {
            System.out.println("el numero es menor");
        }
    }
}