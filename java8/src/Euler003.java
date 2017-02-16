import framework.EulerProblem;
import primes.FactorMap;

import java.util.Comparator;

/**
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143 ?
 *
 * Created by gcharles on 8/17/16.
 */
public class Euler003 extends EulerProblem<Long> {
    @Override
    public long solve( Long input ) {
        FactorMap fm = FactorMap.factor( input );
        return fm.factors().stream().max(Comparator.naturalOrder()).get();
    }
}