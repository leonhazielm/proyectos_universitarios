public class Comida extends Producto {
    private String tipo;
    public Comida(int id, String nombre, double precio, String tipo) {
        super(id, nombre, precio);
        String tipoMinusculas = tipo.toLowerCase();
        if (tipoMinusculas.equals("entrada") ||
                tipoMinusculas.equals("plato fuerte") ||
                tipoMinusculas.equals("postre")) {

            this.tipo = tipoMinusculas;

        } else {
            System.out.println(" Advertencia en el ID " + id + ": El tipo '" + tipo + "' no es válido. Opciones válidas: entrada, plato fuerte, postre.");
            this.tipo = "No definido";
        }
    }


    public String mostrarInformacion() {
        return super.mostrarInformacion() +
                "\n Tipo: " + this.tipo +
                "\n Precio a pagar: $" + calcularPrecioFinal();
    }
}