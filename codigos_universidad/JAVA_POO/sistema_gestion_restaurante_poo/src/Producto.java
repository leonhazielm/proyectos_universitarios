public class Producto {
    protected int  id;
    protected String nombre;
    protected double precio;
    public Producto(int id, String nombre, double precio) {
        this.id = id;
        this.nombre = nombre;
        this.precio = precio;
    }
    String mostrarInformacion() {
        return "ID del producto: " + id + "\nNombre: " + nombre + "\nPrecio: " + precio;
    }
    public double calcularPrecioFinal() {
        return precio;
    }
}
