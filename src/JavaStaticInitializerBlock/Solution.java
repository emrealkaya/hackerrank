package JavaStaticInitializerBlock;

import java.util.Scanner;

public class Solution {

    static int B, H;
    static boolean flag = true;

    static {
        Scanner sc = new Scanner(System.in);
        int B = sc.nextInt();
        int H = sc.nextInt();
        try {
            if (B <= 0 || H <= 0)
                throw new Exception("Breath and height must be positive");

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}


