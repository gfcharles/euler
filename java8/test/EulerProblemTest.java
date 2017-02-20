import framework.EulerProblem;
import org.junit.jupiter.api.Test;

import java.util.Optional;
import java.util.OptionalInt;
import java.util.OptionalLong;

import static org.junit.jupiter.api.Assertions.assertEquals;


/**
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
                            T realInput, OptionalLong realSolution)
    {
        this.eulerProblem = eulerProblem;
        this.testInput = testInput;
        this.testSolution = testSolution;
        this.realInput = realInput;
        this.realSolution = realSolution;
    }

    public EulerProblemTest(EulerProblem<T> eulerProblem, T realInput, OptionalLong realSolution) {
        this( eulerProblem, Optional.empty(), OptionalLong.empty(), realInput, realSolution );
    }

    @Test
    public void testSolve() {
        testSolution.ifPresent(solution -> assertEquals( solution, eulerProblem.solve(testInput.get()) ));
        realSolution.ifPresent(solution -> assertEquals( solution, eulerProblem.solve(realInput) ));
        System.out.println( this.eulerProblem.getClass().getSimpleName() + " Solution = "
                + realSolution.orElseGet(() -> eulerProblem.solve(realInput) ));
    }

}
