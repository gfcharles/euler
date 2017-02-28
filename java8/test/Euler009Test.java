import java.util.Optional;
import java.util.OptionalLong;

/**
 * Test for Project Euler, problem 9.
 */
class Euler009Test extends EulerProblemTest<Integer> {
    public Euler009Test() {
        super(new Euler009(), Optional.of(3 + 4 + 5), OptionalLong.of(3 * 4 * 5),1000,
                OptionalLong.of(31_875_000));
    }
}