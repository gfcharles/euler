import framework.EulerProblem;
import util.MathUtils;

import static java.util.stream.LongStream.range;

/**
 * A palindromic number reads the same both ways. The largest palindrome made from the product of
 * two 2-digit numbers is 9009 = 91 × 99.
 * <p>
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */
public class Euler004 extends EulerProblem<Integer> {
    @Override
    public long solve(Integer digits) {

        long min = (long) Math.pow(10, digits - 1);
        long max = (long) Math.pow(10, digits);

        return range(min, max)
                .flatMap(a -> range(a, max)
                        .map(b -> a * b))
                .filter(MathUtils::isPalindrome)
                .max()
                .orElse(0L);
    }
}