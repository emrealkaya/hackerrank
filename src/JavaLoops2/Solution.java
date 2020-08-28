package JavaLoops2;

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int u = sc.nextInt();
        for (int i = 0; i < u; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int n = sc.nextInt();

            for (int j = 0; j < n; j++) {
                a += b;
                if (j > 0)
                    System.out.print(" ");
                System.out.print(a);
                b *= 2;

            }
            System.out.println("");
        }
    }
}
