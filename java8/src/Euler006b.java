import framework.EulerProblem;

import java.util.function.Supplier;
import java.util.stream.LongStream;

/**
 * The sum of the squares of the first ten natural numbers is,
 * <p>
 * 1^2 + 2^2 + ... + 10^2 = 385
 * The square of the sum of the first ten natural numbers is,
 * <p>
 * (1 + 2 + ... + 10) ^ 2 = 55 ^ 2 = 3025
 * Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
 * 3025 − 385 = 2640.
 * <p>
 * Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
 */
public class Euler006b extends EulerProblem<Integer> {
    @Override
    public long solve(Integer max) {
        Supplier<LongStream> range = () -> LongStream.rangeClosed(1, max);

        return squareOfSum(range) - sumOfSquares(range);
    }

    private long sumOfSquares(Supplier<LongStream> range) {
        return range
                .get()
                .map(n -> n * n)
                .sum();
    }

    private long squareOfSum(Supplier<LongStream> range) {
        return range.get().sum() * range.get().sum();
    }
}