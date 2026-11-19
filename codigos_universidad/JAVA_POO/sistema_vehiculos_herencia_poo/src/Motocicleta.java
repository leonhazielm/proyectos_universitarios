public class Motocicleta extends vehiculo {
    private int cilindraje ;
    public Motocicleta(String marca , String modelo , int año , int cilindraje) {
        super(marca , modelo , año );
        this.cilindraje = cilindraje;
    }
    public String mostrarInformacion() {
        return super.mostrarInformacion() + "\ncilindraje :" + cilindraje ;
    }
     public double calcularMantenimiento() {
        return 500.00 ;
    }

}
