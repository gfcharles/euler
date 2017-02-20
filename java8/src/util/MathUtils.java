package util;

/**
 * Created by gcharles on 2/17/17.
 */
public class MathUtils {
    public static boolean isPalindrome(int n) {
        String s = String.valueOf(n);
        return new StringBuilder(s).reverse().toString().equals(s);
    }
}
