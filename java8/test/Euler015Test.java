import org.apache.commons.lang3.tuple.ImmutablePair;
import org.apache.commons.lang3.tuple.Pair;

import java.util.Optional;
import java.util.OptionalLong;


public class Euler015Test extends EulerProblemTest<Pair<Integer, Integer>> {
    public Euler015Test() {
        super(new Euler015(),
                Optional.of(new ImmutablePair<>(2, 2)), OptionalLong.of( 6L ),
                new ImmutablePair<>(20, 20), OptionalLong.of( 137846528820L ));
    }
}