import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class giatritbcuamang {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Chương trình tính giá trị trung bình của mảng gồm n phần tử số nguyên\n--------------------");
        System.out.println("Nhập n: ");
        int n = sc.nextInt();
        int tong = 0;
        List <String> A = new ArrayList<>();
        for (int i = 1; i <= n; i++){
            tong = tong + i;
            A.add(String.valueOf(i));
        }
        String listA = String.join(" , ", A);
        float tb = (float)tong / n;
        System.out.println("Giá trị trung bình của mảng [ #listA ] là #tb".replaceAll("#listA", listA).replaceAll("#tb", String.valueOf(tb)));
    }
}
