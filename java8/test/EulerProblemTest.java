import framework.EulerProblem;
import org.junit.Test;

import java.util.Optional;
import java.util.OptionalLong;

import static org.junit.Assert.assertEquals;

/**
 * Base class for Euler Problem tests.
 * Created by gcharles on 2/12/17.
 */
public abstract class EulerProblemTest<T> {
    private final EulerProblem<T> eulerProblem;
    private final Optional<T> testInput;
    private final OptionalLong testSolution;
    private final T realInput;
    private final OptionalLong realSolution;

    public EulerProblemTest(EulerProblem<T> eulerProblem,
                            Optional<T> testInput, OptionalLong testSolution,
                            T realInput, OptionalLong realSolution) {

        this.eulerProblem = eulerProblem;
        this.testInput = testInput;
        this.testSolution = testSolution;
        this.realInput = realInput;
        this.realSolution = realSolution;
    }

    public EulerProblemTest(EulerProblem<T> eulerProblem, T realInput, OptionalLong realSolution) {
        this(eulerProblem, Optional.empty(), OptionalLong.empty(), realInput, realSolution);
    }

    public EulerProblemTest(EulerProblem eulerProblem, T testInput, long testSolution, T realInput) {
        this(eulerProblem, Optional.of(testInput), OptionalLong.of(testSolution), realInput, OptionalLong.empty());
    }

    public EulerProblemTest(EulerProblem eulerProblem, T testInput, long testSolution, T realInput, long realSolution) {
        this(eulerProblem, Optional.of(testInput), OptionalLong.of(testSolution),
                realInput, OptionalLong.of(realSolution));
    }

    public EulerProblemTest(EulerProblem eulerProblem, T realInput) {
        this(eulerProblem, Optional.empty(), OptionalLong.empty(), realInput, OptionalLong.empty());
    }

    public EulerProblemTest(EulerProblem eulerProblem, T realInput, long realSolution) {
        this(eulerProblem, Optional.empty(), OptionalLong.empty(), realInput, OptionalLong.of(realSolution));
    }

    @Test
    public void testSolve() {
        testSolution.ifPresent(solution -> assertEquals(solution, eulerProblem.solve(testInput.get())));
        realSolution.ifPresent(solution -> assertEquals(solution, eulerProblem.solve(realInput)));
        System.out.println(this.eulerProblem.getClass().getSimpleName() + " Solution = "
                + realSolution.orElseGet(() -> eulerProblem.solve(realInput)));
    }

}
