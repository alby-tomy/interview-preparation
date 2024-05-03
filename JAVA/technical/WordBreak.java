import java.util.*;

public class WordBreak {
    public static void main(String[] args) {
        Set<String> dictionary = new HashSet<>(Arrays.asList("i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"));
        
        System.out.println("Input: ilikesamsung");
        List<String> segmentations = segmentString("ilikesamsung", dictionary);
        for (String segmentation : segmentations) {
            System.out.println("Output: " + segmentation);
        }
    }

    public static List<String> segmentString(String s, Set<String> dictionary) {
        int n = s.length();
        List<String>[] dp = new ArrayList[n + 1];
        dp[0] = new ArrayList<>();
        dp[0].add("");

        for (int i = 1; i <= n; i++) {
            dp[i] = new ArrayList<>();
            for (int j = 0; j < i; j++) {
                String word = s.substring(j, i);
                if (dp[j].size() > 0 && dictionary.contains(word)) {
                    for (String segment : dp[j]) {
                        dp[i].add(segment.isEmpty() ? word : segment + " " + word);
                    }
                }
            }
        }

        return dp[n];
    }
}
