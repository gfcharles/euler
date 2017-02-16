import java.util.Optional;
import java.util.OptionalLong;

/**
 * Created by gcharles on 2/12/17.
 */
class Euler003Test extends EulerProblemTest<Long> {
    public Euler003Test() {
        super(new Euler003(), Optional.of(13195L), OptionalLong.of(29), 600851475143L, OptionalLong.of(6857));
    }
}