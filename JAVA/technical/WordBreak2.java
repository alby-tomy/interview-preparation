public class WordBreak2 {
    public static void main(String[] args) {
        String[] dictionary = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"};
        
        System.out.println("Input: ilikesamsung");
        segmentString("ilikesamsung", dictionary);
    }

    public static void segmentString(String s, String[] dictionary) {
        segmentStringHelper(s, dictionary,  0, "");
    }

    private static void segmentStringHelper(String s, String[] dictionary, int start, String result) {
        if (start == s.length()) {
            System.out.println("Output: " + result);
            return; 
        }

        for (int end = start + 1; end <= s.length(); end++) {
            String word = s.substring(start, end);
            if (isWordInDictionary(word, dictionary)) {
                String newResult = result.isEmpty() ? word : result + " " + word;
                segmentStringHelper(s, dictionary, end, newResult);
            }
        }
    }

    private static boolean isWordInDictionary(String word, String[] dictionary) {
        for (String dictWord : dictionary) {
            if (dictWord.equals(word)) {
                return true;
            }
        }
        return false;
    }
}
