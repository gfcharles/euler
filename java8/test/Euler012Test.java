import java.util.Optional;
import java.util.OptionalLong;

/**
 * Created by gcharles on 2/12/17.
 */
class Euler012Test extends EulerProblemTest<Integer> {
    public Euler012Test() {
        super(new Euler012(), Optional.of(5), OptionalLong.of(28), 500, OptionalLong.of(76576500));
    }
}