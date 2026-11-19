public class Libro extends Material{
    private int paginas;
    public Libro(String titulo, String autor , int año, int paginas) {
        super(titulo, autor, año);
        this.paginas = paginas;
    }
    public String mostrarInformacion() {
        return super.mostrarInformacion() + " paginas :" + paginas;
    }
}
