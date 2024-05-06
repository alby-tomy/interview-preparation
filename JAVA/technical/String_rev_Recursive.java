public class String_rev_Recursive {

    public static String reverseString(String str) {
        if (str.isEmpty())
            return str;
        return reverseString(str.substring(1)) + str.charAt(0);
    }

    // Example usage
    public static void main(String[] args) {
        String reversedStr = reverseString("Hello");
        System.out.println(reversedStr); // Output: "olleH"
    }

}
