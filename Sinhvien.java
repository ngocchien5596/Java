public class Sinhvien {
    int id;
    String ten;
    void themSV(int id, String ten){
        this.id = id;
        this.ten = ten;
    }
    void hienThiSV (){
        System.out.println(id+" "+ten);
    }
    public static void main(String[] args) {
        Sinhvien sv1 = new Sinhvien();
        sv1.themSV(1,"Bui Ngoc Chien");
        sv1.hienThiSV();
    }
}
