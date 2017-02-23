import java.util.Optional;
import java.util.OptionalLong;

/**
 * Test for Project Euler, problem 7.
 */
class Euler007Test extends EulerProblemTest<Integer> {
    public Euler007Test() {
        super(new Euler007(), Optional.of(6), OptionalLong.of(13), 10_001, OptionalLong.of(104743));
    }
}