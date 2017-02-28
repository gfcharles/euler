import framework.EulerProblem;

import java.util.stream.IntStream;

/**
 * A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
 * <p>
 * a^2 + b^2 = c^2
 * For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
 * <p>
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 */
public class Euler009 extends EulerProblem<Integer> {
    @Override
    public long solve(Integer sum) {
        // Notes:u
        // Since a^2 + b^2 = c^2 and a + b + c == sum
        // it follows that:
        // b = (sum^2 - 2 * sum * a) / (2 * sum - 2 * a)
        // The solution will be any a, b where a, b > 0 and both integers.
        return IntStream.range(1, sum)
                .filter(a -> ((sum * sum) - 2 * sum * a) % (2 * sum - 2 * a) == 0)
                .map(a -> {
                    int b = ((sum * sum) - 2 * sum * a) / (2 * sum - 2 * a);
                    int c = sum - a - b;
                    return a * b * c;
                })
                .findFirst()
                .getAsInt();
    }

}