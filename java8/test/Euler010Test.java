import java.util.Optional;
import java.util.OptionalLong;

/**
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 * <p>
 * Find the sum of all the primes below two million.
 */
public class Euler010Test extends EulerProblemTest<Integer> {
    public Euler010Test() {
        super(new Euler010(), 10, 17, 2_000_000, 142_913_828_922L);
    }
}