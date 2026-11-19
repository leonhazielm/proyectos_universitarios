import java.util.Scanner;

public class random {
    // 1. Atributos
    int numeroSecreto;
    int contadorIntentos;
    int[] historial = new int[20];

    // 2. Constructor
    public random() {
        this.contadorIntentos = 0;
        this.numeroSecreto = (int)(Math.random() * 50) + 1;
    }

    // 3. Me
    // todo jugar()
    public void jugar() {
        Scanner leer = new Scanner(System.in);
        for (int i = 0; i < 20; i++) {
            System.out.println("Adivina el número (del 1 al 50):");
            int intentoUsuario = leer.nextInt();

            this.historial[i] = intentoUsuario;
            this.contadorIntentos++;

            if (intentoUsuario == this.numeroSecreto) {
                System.out.println("Felicidades adivinaste :) Te tomó " + this.contadorIntentos + " intentos.");
                break;
            } else {
                System.out.println("Fallaste, vuelve a intentarlo.");
            }
        }
    }

    // 4. Método mostrarHistorial()
    public void mostrarHistorial() {
        System.out.println("Tus intentos fueron:");
        for (int i = 0; i < 20; i++) {
            if (this.historial[i] != 0) {
                System.out.println(this.historial[i]);
            }
        }
    }
}