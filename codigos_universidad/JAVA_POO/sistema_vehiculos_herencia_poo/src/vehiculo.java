public class vehiculo {
    protected String marca;
    protected String modelo;
    protected int año ;
    public vehiculo(String marca, String modelo , int año) {
        this.marca = marca;
        this.modelo = modelo;
        this.año = año ;
    }
    public String mostrarInformacion() {
        return "Modelo:" +  modelo  + "\nMarca:" + marca + "\nAno:" + año ;

    }
    public double calcularMantenimiento() {
        return 00.00 ;
    }
}
