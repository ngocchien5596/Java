import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class timminmax2 {
    public static void tim_min(List <Integer> A,int n) {
        int min = 0;
        min =  A.get(0);
        for (int i = 0; i < n; i++){
            if (min > A.get(i)){
                min = A.get(i);
            }
        }
        System.out.println("Giá trị nhỏ nhất là: "+min);
    }
    public static void tim_max(List <Integer> A,int n) {
        int max = 0;
        max =  A.get(0);
        for (int i = 0; i < n; i++){
            if ( max < A.get(i)){
                 max = A.get(i);
            }
        }
        System.out.println("Giá trị lớn nhất là: "+max);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Chương trình tìm Min, Max của dãy số nhập từ bàn phím\n--------------------");
        System.out.print("Nhập độ dài dãy số: ");
        int n = sc.nextInt();
        List <Integer> A = new ArrayList<>();
        for (int i = 0; i < n; i++){
            System.out.print("Nhập số thứ #i: ".replaceAll("#i", String.valueOf(i+1)));
            A.add(sc.nextInt());
        }
        tim_min(A,n);
        tim_max(A,n);
       
    }
    
}
