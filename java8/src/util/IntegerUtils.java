package util;

/**
 * Created by gcharles on 2/12/17.
 */
public class IntegerUtils {
    public static boolean even(long l) {
        return (l & 1) == 0;
    }

    public static boolean odd(long l) {
        return (l & 1) == 1;
    }
}
