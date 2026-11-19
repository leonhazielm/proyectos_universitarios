public class Automovil extends vehiculo {
    private int Puertas;
    public Automovil(String marca , String modelo , int año , int Puertas) {
        super(marca , modelo , año);
        this.Puertas = Puertas;
    }
    public String mostrarInformacion() {
        return super.mostrarInformacion() + "\npuertas :" + Puertas;
    }
    public double calcularMantenimiento() {
        return 1000.00 ;
    }
}
