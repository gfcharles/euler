import java.util.Optional;
import java.util.OptionalLong;

/**
 * Created by gcharles on 2/12/17.
 */
class Euler004Test extends EulerProblemTest<Integer> {
    public Euler004Test() {
        super(new Euler004(), Optional.of(2), OptionalLong.of(9009), 3, OptionalLong.of(906609));
    }
}