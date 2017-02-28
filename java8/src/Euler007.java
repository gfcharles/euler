import framework.EulerProblem;
import primes.PrimeSupplier;

import java.util.stream.IntStream;
import java.util.stream.LongStream;

/**
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 * <p>
 * What is the 10 001st prime number?
 */
public class Euler007 extends EulerProblem<Integer> {
    @Override
    public long solve(Integer pos) {
        return IntStream.generate(new PrimeSupplier())
                .skip(pos - 1)
                .findFirst()
                .getAsInt();
    }
}