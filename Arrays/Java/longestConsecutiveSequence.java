package Arrays.Java;

import java.util.HashSet;

public class longestConsecutiveSequence {
    public static void main(String[] args) {
        int[] nums = { 9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6, 234 };
        System.out.println(maxSequence(nums));

    }

    public static int maxSequence(int[] arr) {
        HashSet<Integer> checker = new HashSet<>();
        int ans = 0;
        for (int num : arr) {
            checker.add(num);
        }

        for (int i = 0; i < arr.length; i++) {
            if (!checker.contains(arr[i] - 1)) {

                int count = 1;
                while (checker.contains(count + arr[i])) {
                    count++;
                    ans = Math.max(count, ans);
                }
            }
        }

        return ans;
    }

}
