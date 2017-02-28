import framework.EulerProblem;

import java.util.stream.IntStream;

/**
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
 * The sum of these multiples is 23.
 * <p>
 * Find the sum of all the multiples of 3 or 5 below 1000.
 * <p>
 * Created by gcharles on 2/12/17.
 */
public class Euler001 extends EulerProblem<Integer> {

    @Override
    public long solve(Integer input) {
        return IntStream.range(1, input)
                .filter(n -> n % 3 == 0 || n % 5 == 0)
                .sum();
    }
}
