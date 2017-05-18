import java.util.Optional;
import java.util.OptionalLong;

/**
 * Created by gcharles on 2/12/17.
 */
public class Euler001Test extends EulerProblemTest<Integer> {
    public Euler001Test() {
        super(new Euler001(), Optional.of(10), OptionalLong.of(23), 1000, OptionalLong.of(233168));
    }
}