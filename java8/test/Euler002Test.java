import framework.EulerProblem;

import java.util.OptionalLong;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Created by gcharles on 2/12/17.
 */
class Euler002Test extends EulerProblemTest {
    public Euler002Test() {
        super(new Euler002(), 4_000_000, OptionalLong.of(4_613_732));
    }
}