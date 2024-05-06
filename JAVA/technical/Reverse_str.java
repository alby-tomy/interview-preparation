public class Reverse_str {
    public static void main(String[] args) {
        String str = "Hello";
        char[] charArray = str.toCharArray();
        int start = 0;
        int end = charArray.length - 1;
        while (start < end) {
            char temp = charArray[start];
            charArray[start] = charArray[end];
            charArray[end] = temp;
            start++;
            end--;
        }
        String reversedStr = new String(charArray);
        System.out.println(reversedStr); // Output: "olleH"

    }

}
