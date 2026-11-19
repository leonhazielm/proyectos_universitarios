import java.util.ArrayList;

public class Orden {
    private Cliente cliente;
    private ArrayList<Producto> listaproductos;
    private double totalOrden;

    public Orden(Cliente cliente) {
        this.cliente = cliente;
        this.listaproductos = new ArrayList<>();
        this.totalOrden = 0.0;
    }

    public void agregarProducto(Producto producto) {
        this.listaproductos.add(producto);
        System.out.println("Producto agregado: " + producto.nombre);
    }

    public double calcularTotalOrden() {
        double totaltemp = 0;
        for (Producto p : this.listaproductos) {
            totaltemp += p.calcularPrecioFinal();
        }
        this.totalOrden = totaltemp;
        return this.totalOrden;
    }


    public void aplicarDescuento() {
        if (cliente.getTipoCliente().equalsIgnoreCase("frecuente")) {
            double descuento = this.totalOrden * 0.15;
            this.totalOrden -= descuento;
            System.out.println("Descuento aplicado. Nuevo total: $" + this.totalOrden);
        }
    }


    public void mostrarOrden() {
        System.out.println(cliente.mostrarInformacion());
        for (Producto p : this.listaproductos) {
            System.out.print("- " + p.nombre + " | Precio final: $" + p.calcularPrecioFinal());

            if (p.calcularPrecioFinal() > p.precio) {
                System.out.print(" Cargo extra por tamaño");
            }

            System.out.println();
        }


        System.out.println("TOTAL DE LA ORDEN: $" + this.totalOrden);


        if (cliente.getTipoCliente().equalsIgnoreCase("frecuente")) {
            System.out.println(" Se aplicó un 15% de descuento por ser Cliente Frecuente");
        }


    }
    }
