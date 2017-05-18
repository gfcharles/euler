import java.util.Optional;
import java.util.OptionalLong;

/**
 * If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
 * 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 * <p>
 * If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many
 * letters would be used?
 */
public class Euler017Test extends EulerProblemTest<Integer> {
    public Euler017Test() {
        super(new Euler017(), 5, 19, 1000);
    }
}