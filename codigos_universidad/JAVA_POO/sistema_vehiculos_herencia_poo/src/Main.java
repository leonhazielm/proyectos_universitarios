//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
void main() {
    Scanner sc = new Scanner(System.in);
ArrayList<vehiculo> listavehiculos = new ArrayList<>();
    System.out.println("Ingrese los datos de su vehiculo : Modelo , Marca, Ano ");
listavehiculos.add(new vehiculo( sc.next(), sc.next() ,  sc.nextInt()  )) ;
    System.out.println("Ingrese los datos de su AUTOMOVIL : Modelo , Marca , Ano , Puertas ");
listavehiculos.add(new Automovil( sc.next(), sc.next() ,  sc.nextInt() , sc.nextInt() )) ;
    System.out.println("Ingrese los datos de su motocicleta ; Modelo ,Marca , Ano , Cilindraje ");
listavehiculos.add(new Motocicleta(sc.next(), sc.next() ,  sc.nextInt() , sc.nextInt() )) ;
for (vehiculo v : listavehiculos) {
    System.out.println(v.mostrarInformacion());
    System.out.println("Costo de mantenimeinto " + v.calcularMantenimiento());

}
}
