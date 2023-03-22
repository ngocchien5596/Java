import java.util.Scanner;

public class tinhtong {
    // public static void sum(){
    //     Scanner sc = new Scanner(System.in);
    //     System.out.println("Nhập n: ");
    //     int n = sc.nextInt();
    //     int tong= 0;
    //     while (n>0){
    //         for(int i=1; i<=n;i++){
    //             tong=tong+i;
    //         }
    //     }
    //     System.out.println("Tong day so la: "+tong);
    // }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhập n: ");
        int n = sc.nextInt();
        int tong= 0;
        for(int i=1; i<=n;i++){
            tong=tong+i;
        }
        
        System.out.println("Tong day so la: "+tong);
    }
}
