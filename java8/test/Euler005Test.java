import java.util.Optional;
import java.util.OptionalLong;

/**
 * Test for Project Euler, problem 5.
 */
class Euler005Test extends EulerProblemTest<Integer> {
    public Euler005Test() {
        super(new Euler005(), Optional.of(10), OptionalLong.of(2520), 20, OptionalLong.of(232_792_560));
    }
}