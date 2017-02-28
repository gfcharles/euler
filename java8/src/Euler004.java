import framework.EulerProblem;
import org.apache.commons.lang3.tuple.ImmutablePair;
import util.MathUtils;

import java.util.stream.IntStream;

/**
 * A palindromic number reads the same both ways. The largest palindrome made from the product of
 * two 2-digit numbers is 9009 = 91 × 99.
 * <p>
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */
public class Euler004 extends EulerProblem<Integer> {
    @Override
    public long solve(Integer digits) {

        int min = (int) Math.pow(10, digits - 1);
        int max = (int) Math.pow(10, digits);

        return IntStream
                .range(min, max).mapToObj(n -> n)
                .flatMap(e1 -> IntStream.range(min, max).mapToObj(n -> n)
                        .map(e2 -> new ImmutablePair<>(e1, e2)))
//              .peek(System.out::println)
                .mapToInt(pair -> pair.getLeft() * pair.getRight())
                .filter(MathUtils::isPalindrome)
                .max()
                .getAsInt();
    }


}