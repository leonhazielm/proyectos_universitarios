//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
void main() {
    ArrayList<Material> listaMaterial = new ArrayList<>();
    Scanner sc = new Scanner(System.in);
    listaMaterial.add(new Libro("harry potter", "LARA JEAN", 2020, 700));
    System.out.println("Ingrese los datos de su Revista : Titulo , autor, ano de publicacion , numero de edicion");
    listaMaterial.add(new Revista(sc.next(), sc.next(), sc.nextInt(), sc.nextInt()));
    listaMaterial.add(new Revista("Muy Interesante", "Yir", 2022, 60));
    listaMaterial.add(new Revista("FIFA", "Cachetes", 1999, 45));
    listaMaterial.add(new Libro("La Guia del ligue", "Werever", 2030, 987));
    for (Material i : listaMaterial) {
        if (i.getAño() >= 2015) {
            System.out.println(i.mostrarInformacion());
        }
    }
}