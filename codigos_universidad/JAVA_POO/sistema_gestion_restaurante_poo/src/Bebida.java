public class Bebida extends Producto{
private String size ;
public Bebida( int id , String nombre, double precio , String size) {
    super(id , nombre , precio);
    this.size = size;
}
public String mostrarInformacion(){
    return super.mostrarInformacion() + "\n tamaño: " + size + "\n Precio Final : " + calcularPrecioFinal();
}
public double calcularPrecioFinal(){
    double precioFinal = this.precio;
    if (this.size.equalsIgnoreCase("mediano")) {
        precioFinal += 15.0;
    } else if (this.size.equalsIgnoreCase("grande")) {
        precioFinal += 25.0;
    }
    return precioFinal;
}
}

