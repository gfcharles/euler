import framework.EulerProblem;
import util.MathUtils;

import java.util.stream.LongStream;

/**
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

 What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 */
public class Euler005 extends EulerProblem<Integer> {
    @Override
    public long solve( Integer max ) {

        return LongStream
                .range(2, max)
                .reduce(1, MathUtils::lcm );
    }


}