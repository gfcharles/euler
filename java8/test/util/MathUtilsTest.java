package util;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Created by gcharles on 2/20/17.
 */
class MathUtilsTest {
    @Test
    public void testCombinations() {
        assertEquals( 10L, MathUtils.combinations(5, 3));
        assertEquals( 330L, MathUtils.combinations( 11, 7 ));

        assertEquals( 1L, MathUtils.combinations( 6, 6));
        assertEquals( 1L, MathUtils.combinations( 100, 0));
        assertEquals( 1L, MathUtils.combinations( 0, 0));

        assertEquals( 0L, MathUtils.combinations( 2, 5));
        assertEquals( 0L, MathUtils.combinations( 8, -2));
    }

}