public class trabajadores {
    String  nombre;
    float  horas_trabajadas;
    trabajadores(String nombre, float horas_trabajadas) {
        this.nombre = nombre;
        this.horas_trabajadas = horas_trabajadas;
    }
    public float getHoras_trabajadas() {
        float salariofinal = 0;
        if ( horas_trabajadas <= 40 ) {
            salariofinal = horas_trabajadas * 20;
        }
        else {
            float pagoBase = 40 * 20;
            float horasExtra = horas_trabajadas - 40;
            float pagoExtra = horasExtra * 25;

            salariofinal = pagoBase + pagoExtra;
        }

        return salariofinal;
    }
    public void imprimirRecibo() {
        System.out.println("Obrero: " + nombre + " | Horas: " + horas_trabajadas + " | Salario: $" + getHoras_trabajadas());

        }
    }

