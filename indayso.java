import java.util.Scanner;

public class indayso {
    public static void main(String[] args) {
        System.out.println("Nhập số tự nhiên cuối cùng: ");
        Scanner sc = new Scanner(System.in);
        int so = sc.nextInt();
        System.out.println("Dãy số tự nhiên từ 0 đến " + so + " là: ");
        for (int i = 0; i <= so; i++){
            System.out.print(i+" ");
        }

    }
}
