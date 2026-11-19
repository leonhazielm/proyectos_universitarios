public class Material {
     protected String titulo;
     protected String autor;
     protected int año ;
     public Material(String titulo , String autor , int año) {
         this.titulo = titulo;
         this.autor = autor;
         this.año = año ;
     }
    public String mostrarInformacion() {
        return "Autor: " + this.autor + "\n" + "Titulo: " + this.titulo + "\n" + "ano de publicacion : " + this.año + "\n";
    }
    public int getAño() {
         return this.año;
    }
    }

