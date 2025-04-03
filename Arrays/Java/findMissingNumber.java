package Arrays.Java;

import java.util.Arrays;

public class findMissingNumber {

    public static void main(String[] args) {

        int[] arr = { 2, 1, 5, 3 };
        System.out.println(missingNumer(arr));

    }

    public static int missingNumer(int[] arr) {

        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));

        int n = arr[arr.length - 1];
        int xor1 = 0;
        for (int i = 0; i <= n; i++) {
            xor1 ^= i;
        }
        int xor2 = 0;
        for (int i = 0; i < arr.length; i++) {
            xor2 ^= arr[i];
        }

        return xor1 ^ xor2;
    }
}