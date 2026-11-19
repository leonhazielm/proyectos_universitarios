public class Cliente {
    private int id;
    private String nombre;
    private String tipoCliente;
    public Cliente(int id, String nombre, String tipoCliente) {
        this.id = id;
        this.nombre = nombre;
        String tipoMinusculas = tipoCliente.toLowerCase();
        if (tipoMinusculas.equals("normal") || tipoMinusculas.equals("frecuente")) {
            this.tipoCliente = tipoMinusculas;
        } else {
            System.out.println(" Advertencia: El tipo de cliente '" + tipoCliente + "' no es válido. Opciones: normal, frecuente.");
            this.tipoCliente = "normal";
        }
    }
    public String mostrarInformacion() {
        return "--- Datos del Cliente ---" +
                "\n ID: " + this.id +
                "\n Nombre: " + this.nombre +
                "\n Tipo de Cliente: " + this.tipoCliente;
    }
    public String getTipoCliente() {
        return tipoCliente;
    }
}