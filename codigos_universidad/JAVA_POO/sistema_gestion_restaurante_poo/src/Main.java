import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Producto> menuRestaurante = new ArrayList<>();
        ArrayList<Cliente> listaDeClientes = new ArrayList<>();
        ArrayList<Orden> listaDeOrdenes = new ArrayList<>(); // ¡Nueva lista para guardar las órdenes!

        int opcion = 0;

        while (opcion != 8) {
            System.out.println("1. Registrar Producto");
            System.out.println("2. Registrar Cliente");
            System.out.println("3. Crear Orden");
            System.out.println("4. Agregar Producto a Orden");
            System.out.println("5. Mostrar Órdenes");
            System.out.println("6. Mostrar Clientes");
            System.out.println("7. Total del Día");
            System.out.println("8. Salir");
            System.out.print("Elige una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine();
            switch (opcion) {
                case 1:
                    System.out.print("¿Qué deseas registrar? (1: Bebida, 2: Comida): ");
                    int tipoProd = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("ID del producto: ");
                    int idProd = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Nombre: ");
                    String nombreProd = scanner.nextLine();
                    System.out.print("Precio base: ");
                    double precioProd = scanner.nextDouble();
                    scanner.nextLine();

                    if (tipoProd == 1) {
                        System.out.print("Tamaño (chico, mediano, grande): ");
                        String tamano = scanner.nextLine();
                        menuRestaurante.add(new Bebida(idProd, nombreProd, precioProd, tamano));
                        System.out.println(" Bebida registrada.");
                    } else if (tipoProd == 2) {
                        System.out.print("Tipo (entrada, plato fuerte, postre): ");
                        String tipoComida = scanner.nextLine();
                        menuRestaurante.add(new Comida(idProd, nombreProd, precioProd, tipoComida));
                        System.out.println(" Comida registrada.");
                    }
                    break;

                case 2:
                    System.out.print("ID del cliente: ");
                    int idCli = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Nombre del cliente: ");
                    String nombreCli = scanner.nextLine();
                    System.out.print("Tipo (normal o frecuente): ");
                    String tipoCli = scanner.nextLine();

                    listaDeClientes.add(new Cliente(idCli, nombreCli, tipoCli));
                    System.out.println(" Cliente registrado.");
                    break;

                case 3:
                    if (listaDeClientes.isEmpty()) {
                        System.out.println("Error: No hay clientes registrados. Registra un cliente primero.");
                        break;
                    }

                    System.out.println("Selecciona un cliente por su número en la lista:");
                    for (int i = 0; i < listaDeClientes.size(); i++) {
                        System.out.println((i + 1) + ". Cliente ID: " + listaDeClientes.get(i).mostrarInformacion());
                    }
                    System.out.print("Número de cliente: ");
                    int indiceCliente = scanner.nextInt() - 1;
                    scanner.nextLine();

                    if (indiceCliente >= 0 && indiceCliente < listaDeClientes.size()) {
                        Orden nuevaOrden = new Orden(listaDeClientes.get(indiceCliente));
                        listaDeOrdenes.add(nuevaOrden);
                        System.out.println(" Orden creada. Es la orden #" + listaDeOrdenes.size());
                    } else {
                        System.out.println(" Cliente no válido.");
                    }
                    break;

                case 4:

                    if (listaDeOrdenes.isEmpty() || menuRestaurante.isEmpty()) {
                        System.out.println("️ Error: Debes tener al menos una orden creada y productos en el menú.");
                        break;
                    }

                    System.out.print("¿A qué número de orden deseas agregar productos? (1 a " + listaDeOrdenes.size() + "): ");
                    int numOrden = scanner.nextInt() - 1;
                    scanner.nextLine();

                    if (numOrden >= 0 && numOrden < listaDeOrdenes.size()) {
                        Orden ordenSeleccionada = listaDeOrdenes.get(numOrden);

                        System.out.println("Selecciona el producto:");
                        for (int i = 0; i < menuRestaurante.size(); i++) {
                            System.out.println((i + 1) + ". " + menuRestaurante.get(i).nombre);
                        }
                        System.out.print("Número de producto: ");
                        int numProd = scanner.nextInt() - 1;
                        scanner.nextLine();

                        if (numProd >= 0 && numProd < menuRestaurante.size()) {
                            ordenSeleccionada.agregarProducto(menuRestaurante.get(numProd));

                            ordenSeleccionada.calcularTotalOrden();
                            ordenSeleccionada.aplicarDescuento();
                        } else {
                            System.out.println(" Producto inexistente.");
                        }
                    } else {
                        System.out.println(" Orden inexistente.");
                    }
                    break;

                case 5:

                    System.out.println("\n TODAS LAS ÓRDENES: ");
                    for (int i = 0; i < listaDeOrdenes.size(); i++) {
                        System.out.println(" ORDEN #" + (i + 1));
                        listaDeOrdenes.get(i).mostrarOrden();
                    }
                    break;

                case 6:

                    System.out.println("\n LISTA DE CLIENTES :");
                    for (Cliente c : listaDeClientes) {
                        System.out.println(c.mostrarInformacion());
                    }
                    break;

                case 7:

                    double totalDia = 0;
                    for (Orden orden : listaDeOrdenes) {

                        totalDia += orden.calcularTotalOrden();
                    }
                    System.out.println("\n EL TOTAL DE VENTAS DEL DÍA ES: " + totalDia);
                    break;

                case 8:
                    break;

                default:
                    System.out.println("Opción inválida.");
            }
        }
    }
}