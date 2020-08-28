package JavaStdinAndStdout2;

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        double c = sc.nextDouble();
        sc.nextLine();
        String b = sc.nextLine();

        System.out.println("String: " + b);
        System.out.println("Double: " + c);
        System.out.println("Int: " + a);


    }
}
