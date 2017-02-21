import framework.EulerProblem;

import java.math.BigInteger;

/**
 * 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

 What is the sum of the digits of the number 2^1000?
 */
public class Euler016 extends EulerProblem<Integer> {
    @Override
    public long solve( Integer exp ) {
        return BigInteger.valueOf( 2 ).pow( exp ).toString()
                .chars()
                .map(c -> c - '0')
                .sum();
    }
}