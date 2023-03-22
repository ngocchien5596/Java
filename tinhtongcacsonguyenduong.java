import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class tinhtongcacsonguyenduong {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Tính tổng các số nguyên dương chẵn từ 0 - n");
        System.out.print("Nhập n: ");
        int n = sc.nextInt();
        int tong = 0;
        // int [] A =  new int [n+1];
        List<String> A = new ArrayList<>();
        for (int i = 0; i <= n; i++){
            if (i % 2 ==0 ){
                tong += i;
                A.add(String.valueOf(i));
            }
        }
        String textSummary = String.join(" + ", A);
        System.out.print("Tổng của các số chẵn từ 0 - #n : #textSummary là #tong".replaceAll("#n", String.valueOf(n)).replaceAll("#textSummary",textSummary).replaceAll("#tong", String.valueOf(tong)));
}
}
