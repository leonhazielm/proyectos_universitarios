import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println(" REGISTRO DE CLIENTE");
        System.out.print("Ingrese el nombre del cliente: ");
        String nombreIngresado = scanner.nextLine();
        Cliente cliente1 = new Cliente(nombreIngresado);
        Cliente cliente2 = new Cliente();
        System.out.println(" REPORTE DE CLIENTES REGISTRADOS ");
        System.out.println("Registro 1 (Datos ingresados):");
        cliente1.mostrarInfo();
        System.out.println("Registro 2 (Cliente anónimo/vacío):");
        cliente2.mostrarInfo();
    }
}




















