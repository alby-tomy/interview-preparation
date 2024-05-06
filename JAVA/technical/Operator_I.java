public class Operator_I {
    public static void main(String[] args) {
        int p = 10;
        int q = 7;

        int x = (++p) + (p++) + (--q) + (q--);
        int y = (--q) + (q++) + (--p) + (p++);

        // x = (++p) + (p++) + (--q) + (q--):
        // ++p: Increment p before using its value, so p becomes 11, and it returns 11.
        // p++: Increment p after using its value, so p becomes 12, but the value used here is still 11.
        // --q: Decrement q before using its value, so q becomes 6, and it returns 6.
        // q--: Decrement q after using its value, so q becomes 5, but the value used here is still 6.
        // x evaluates to 11 + 11 + 6 + 6 = 34.

        // y = (--q) + (q++) + (--p) + (p++):
        // --q: Decrement q before using its value, so q becomes 4, and it returns 4.
        // q++: Increment q after using its value, so q becomes 5, but the value used here is still 4.
        // --p: Decrement p before using its value, so p becomes 11, and it returns 11.
        // p++: Increment p after using its value, so p becomes 12, but the value used here is still 11.
        // y evaluates to 4 + 4 + 11 + 11 = 30.

        System.out.println("p = " + p); // Output: p = 10
        System.out.println("q = " + q); // Output: q = 7
        System.out.println("x = " + x); // Output: x = 30
        System.out.println("y = " + y); // Output: y = 30
    }
}
