package util;

import java.util.stream.LongStream;

/**
 * Created by gcharles on 2/17/17.
 */
public class MathUtils {
    public static boolean isPalindrome(int n) {
        String s = String.valueOf(n);
        return new StringBuilder(s).reverse().toString().equals(s);
    }

    public static long combinations(int n, int m) {
        if ( n < m || n < 0 || m < 0 ) {
            return 0;
        }

        int limit = Math.min( m, n - m );

        return LongStream
                .rangeClosed( 1, limit )
                .reduce(1L, (prod, i) -> prod * (n - i + 1) / i );
    }
}
