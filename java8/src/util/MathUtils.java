package util;

import java.util.stream.LongStream;

/**
 * Various math or math-like utilities for Project Euler.
 * Created by gcharles on 2/17/17.
 */
public class MathUtils {
    public static boolean isPalindrome(int n) {
        String s = String.valueOf(n);
        return new StringBuilder(s).reverse().toString().equals(s);
    }

    public static long combinations(int n, int m) {
        if (n < m || n < 0 || m < 0) {
            return 0;
        }

        int limit = Math.min(m, n - m);

        return LongStream
                .rangeClosed(1, limit)
                .reduce(1L, (prod, i) -> prod * (n - i + 1) / i);
    }

    public static long gcf(long a, long b) {
        while (b > 0) {
            if (a > b) {
                long temp = a;
                a = b;
                b = temp;
            }
            b = b % a;
        }

        return a;
    }

    public static long lcm(long a, long b) {
        return a / gcf(a, b) * b;
    }
}
