package Arrays.Java;

import java.util.HashMap;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class groupAnagram {
    public static void main(String[] args) {
        String[] input_list = { "eat", "tea", "tan", "ate", "nat", "bat" };
        System.out.println(anagrams(input_list));
    }

    public static List<List<String>> anagrams(String[] input_list) {
        HashMap<String, List<String>> map = new HashMap<>();
        for (int i = 0; i < input_list.length; i++) {
            char[] chars = input_list[i].toCharArray();
            Arrays.sort(chars);

            String sortedKey = new String(chars);

            map.putIfAbsent(sortedKey, new ArrayList<>());
            map.get(sortedKey).add(input_list[i]);

        }
        return new ArrayList<>(map.values());
    }
}
