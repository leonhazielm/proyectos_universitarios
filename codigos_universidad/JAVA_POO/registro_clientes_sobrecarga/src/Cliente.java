public class Cliente {
    String nombre;
    int edad;
    String membresia;
    public Cliente() {
        this.nombre = "Consumidor Final";
        this.edad = 18;
        this.membresia = "Básica";
    }
    public Cliente(String nombre) {
        this.nombre = nombre;
        this.edad = 18;
        this.membresia = "Básica";
    }
    public void mostrarInfo() {
        System.out.println("Cliente: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Tipo de Membresía: " + membresia);
    }
}