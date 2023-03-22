import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class timminmax {
    public static void tim_min(int [] A,int n) {
        int min = 0;
        min =  A[0];
        for (int i = 0; i < n; i++){
            if (min > A[i]){
                min = A[i];
            }
        }
        System.out.println("Giá trị nhỏ nhất là :"+min);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Chương trình tìm Min, Max của dãy số nhập từ bàn phím\n--------------------");
        System.out.println("Nhập độ dài dãy số: ");
        int n = sc.nextInt();
        int [] A = new int [n+1];
        for (int i = 0; i < n; i++){
            System.out.println("Nhập số thứ #i".replaceAll("#i", String.valueOf(i+1)));
            A[i] = sc.nextInt();
        }
        tim_min(A,n);
    }
    
}
