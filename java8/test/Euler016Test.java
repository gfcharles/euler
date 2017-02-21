import java.util.Optional;
import java.util.OptionalLong;


class Euler016Test extends EulerProblemTest<Integer> {
    public Euler016Test() {
        super(new Euler016(), Optional.of(15), OptionalLong.of( 26 ), 1000, OptionalLong.of( 1366 ));
    }
}