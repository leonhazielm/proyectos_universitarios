public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.println("¿Cuántos obreros laboran en la empresa?");
    int n = sc.nextInt();
    sc.nextLine();
    trabajadores[] listaObreros = new trabajadores[n];

    for (int i = 0; i < n; i++) {
        System.out.println("Registro del obrero " + (i + 1));

        System.out.print("Nombre: ");
        String nombre = sc.nextLine();

        System.out.print("Total de horas trabajadas: ");
        float horas = sc.nextFloat();
        sc.nextLine();

        listaObreros[i] = new trabajadores(nombre, horas);
    }

    System.out.println("SEMANAL");
    for (int i = 0; i < listaObreros.length; i++) {
        listaObreros[i].imprimirRecibo();
    }
}