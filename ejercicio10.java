import java.util.Scanner;

public class ejercicio10 {public static void main(String[] args) {
    int Saldo = 10000;
    System.out.print("Su saldo es de: ");
    System.out.println(Saldo);
    int Retiro;
    Scanner input = new Scanner(System.in);
    System.out.print("Ingresa la cantidad a retirar: ");
    Retiro = input.nextInt();

    if(Retiro > Saldo){
        System.out.println("El retiro es inposible");
    }
    else {
        System.out.println("Retiro completado");
        System.out.print("Saldo Final es de: ");
        System.out.print(Saldo-Retiro);
    }
}
}