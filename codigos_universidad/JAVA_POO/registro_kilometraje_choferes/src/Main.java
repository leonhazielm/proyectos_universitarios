void main() {
    Scanner input = new Scanner(System.in);
    System.out.print("Ingrese la cantidad de choferes: ");
    int n = input.nextInt();
    input.nextLine();
String[] dias = {"Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"};
choferes[] listachoferes = new choferes[n];
float[] vector = new float[n];

    for (int i = 0; i < n; i++) {
        System.out.print("\nIngrese el nombre del chofer " + (i + 1) + ": ");
String nombre = input.nextLine();

float[] km = new float[6];
        for (int j = 0; j < 6; j++) {
        System.out.print("Km recorridos el " + dias[j] + ": ");
km[j] = input.nextFloat();
        }
                input.nextLine();

listachoferes[i] = new choferes(nombre, km);

vector[i] = listachoferes[i].info();
    }

            System.out.println(" Corte de semana ");
    System.out.printf("%-12s %-7s %-7s %-7s %-7s %-7s %-7s %-7s\n", 
                              "Nombre", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Total");

    for (int i = 0; i < n; i++) {
choferes actual = listachoferes[i];

// 12 espacios para el nombre
        System.out.printf("%-12s ", actual.getNom());

// 7 espacios y 1 decimal para cada día
float[] kmsActuales = actual.getKm();
        for (int j = 0; j < 6; j++) {
        System.out.printf("%-7.1f ", kmsActuales[j]);
        }

                // 7 espacios y 1 decimal para el total
                System.out.printf("%-7.1f\n", vector[i]);
    }
            }