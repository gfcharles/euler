import java.util.Optional;
import java.util.OptionalLong;

/**
 * Test for Project Euler, problem 8.
 */
public class Euler008Test extends EulerProblemTest<Integer> {
    public Euler008Test() {
        super(new Euler008(), Optional.of(4), OptionalLong.of(5_832), 13, OptionalLong.of(23_514_624_000L));
    }
}