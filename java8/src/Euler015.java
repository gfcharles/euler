import framework.EulerProblem;
import org.apache.commons.lang3.tuple.Pair;
import util.MathUtils;

/**
 * Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
 * there are exactly 6 routes to the bottom right corner.
 */
public class Euler015 extends EulerProblem<Pair<Integer, Integer>> {
    @Override
    public long solve(Pair<Integer, Integer> dimensions) {
        return MathUtils.combinations(dimensions.getLeft() + dimensions.getRight(), dimensions.getLeft());
    }
}