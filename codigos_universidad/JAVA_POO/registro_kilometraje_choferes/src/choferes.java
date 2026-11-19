public class choferes {
    private String nom;
    private float[] km;

    public choferes(String nom, float[] km) {
        setNom(nom);
        setKm(km);
    }

    public float info() {
        float suma = 0;
        for(int i = 0; i < km.length; i++) {
            suma += km[i];
        }
        return suma;
    }
    public String getNom() {
        return nom;
    }
    public void setNom(String nom) {
        this.nom = nom;
    }
    public float[] getKm() {
        return km;
    }
    public void setKm(float[] km) {
        this.km = km;
    }
}

