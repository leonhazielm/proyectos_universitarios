public class Revista extends Material {
    private int numero_edicion ;
    public Revista(String titulo , String autor , int año, int numero_edicion) {
        super(titulo , autor , año);
        this.numero_edicion = numero_edicion;
    }
    public String mostrarInformacion() {
        return super.mostrarInformacion() +" numero_edicion :" + numero_edicion;
    }
}
