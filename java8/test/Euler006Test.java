import java.util.Optional;
import java.util.OptionalLong;

/**
 * Test for Project Euler, problem 6.
 */
class Euler006Test extends EulerProblemTest<Integer> {
    public Euler006Test() {
        super(new Euler006(), Optional.of(10), OptionalLong.of(2640), 100, OptionalLong.of(25_164_150));
    }
}