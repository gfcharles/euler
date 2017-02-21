import framework.EulerProblem;
import org.apache.commons.lang3.tuple.ImmutablePair;
import org.apache.commons.lang3.tuple.Pair;

import java.util.Comparator;
import java.util.stream.IntStream;

/**
 * The following iterative sequence is defined for the set of positive integers:

 n → n/2 (n is even)
 n → 3n + 1 (n is odd)

 Using the rule above and starting with 13, we generate the following sequence:

 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
 It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
 proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

 Which starting number, under one million, produces the longest chain?

 NOTE: Once the chain starts the terms are allowed to go above one million.
 */
public class Euler014 extends EulerProblem<Integer> {
    @Override
    public long solve( Integer max ) {
        return IntStream.range( max / 2, max )
                .mapToObj( Euler014::collatzPair )
                .max( Comparator.comparingInt( Pair::getRight ) )
                .get()
                .getLeft();
    }

    private static Pair<Integer, Integer> collatzPair( int input ) {
        return new ImmutablePair<>( input, collatz(input) );
    }

    private static int collatz( int input ) {
        int count = 1;
        long n = input;

        while (n > 1) {
            if ((n & 1) == 1)  {
                n = 3 * n + 1;
            } else {
                n = n / 2;
            }
            ++count;
        }
        return count;
    }
}