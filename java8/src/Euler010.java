import com.protonpack.StreamUtils;
import framework.EulerProblem;
import primes.PrimeSupplier;

import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 * <p>
 * Find the sum of all the primes below two million.
 */
public class Euler010 extends EulerProblem<Integer> {
    @Override
    public long solve(Integer max) {
        // Solution using com.protonpack library: https://github.com/poetix/protonpack
        return StreamUtils
                .takeWhile(PrimeSupplier.primeGenerator(), n -> n < max)
                .collect(Collectors.summingLong(Integer::longValue));
    }
}