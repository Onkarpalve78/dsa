package Arrays.Java;

public class plusOne {
    public static void main(String[] args) {
        int[] digits = { 1, 2, 3 };
        System.out.println(makePlusOne(digits));
    }

    public static int[] makePlusOne(int[] digits) {
        String strnum = "";

        for (int i = 0; i < digits.length; i++) {
            strnum += Integer.toString(digits[i]);
        }

        int num = Integer.parseInt(strnum);
        num++;

        strnum = Integer.toString(num);
        int[] ansarr = new int[strnum.length()];
        for (int i = 0; i < strnum.length(); i++) {
            int digit = Character.getNumericValue(strnum.charAt(i));
            ansarr[i] = digit;
        }

        return ansarr;
    }

}
