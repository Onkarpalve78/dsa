package Java.String;

public class largestOddNumber {
    public static void main(String[] args) {
        String num = "528";
        System.out.println(largestOdd(num));
    }

    public static String largestOdd(String num) {
        String ans = "";

        if (Character.getNumericValue(num.charAt(num.length() - 1)) % 2 != 0) {
            return num;
        }

        for (int i = num.length() - 1; i >= 0; i--) {
            int digit = Character.getNumericValue(num.charAt(i));
            if (digit % 2 != 0) {
                ans = num.substring(0, i + 1);
                return ans;
            }
        }

        return ans;

    }
}
