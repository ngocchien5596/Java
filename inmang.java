import java.util.Scanner;

public class inmang {
    public static void main(String[] args) {
        System.out.print("Nhập số hàng của mảng: ");
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        System.out.print("Nhập số cột của mảng: ");
        int y = sc.nextInt();

        int [][] arr = new int[x][y];
        for (int i=0; i<x; i++){
            for (int j=0; j<y; j++){
                System.out.printf("Nhập phần tử A[%d][%d]: ",i,j);
                arr[i][j] = sc.nextInt();
            }
        }
        for (int i=0; i<x; i++){
            for (int j=0; j<y; j++){
                System.out.print(arr[i][j]+"\t");
            }
            System.out.print("\n");
        }
    }
}
