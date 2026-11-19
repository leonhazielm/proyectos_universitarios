import javax.swing.*;

void main() {
        Scanner sc = new Scanner(System.in);
        int[][] matriz;
        int nfilas, nCol;
        nfilas = Integer.parseInt(JOptionPane.showInputDialog("Introduce el numero de filas"));
        nCol = Integer.parseInt(JOptionPane.showInputDialog("Introduce el numero de columnas"));
        matriz = new int[nfilas][nCol];
        int contadorCeros = 0;

        System.out.println(" Introduce los valores de la matriz del 0 al 9");
        for (int i = 0; i < nfilas; i++) {
            for (int j = 0; j < nCol; j++) {

                int valor;
                while (true) {
                    System.out.print("Matriz [" + i + "][" + j + "]: ");
                    valor = sc.nextInt();

                    if (valor >= 0 && valor <= 9) {
                        break;
                    } else {
                        System.out.println("Error: El valor debe estar estrictamente entre 0 y 9. Intenta de nuevo.");
                    }
                }
                matriz[i][j] = valor;
                if (matriz[i][j] == 0) {
                    contadorCeros++;
                }
            }
        }
        System.out.println(" El valor de la matriz es:");
        for (int i = 0; i < nfilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.print(matriz[i][j] + " ");
            }
        }
        System.out.println("\nEl resultado de la cantidad de ceros es: " + contadorCeros);
    }
