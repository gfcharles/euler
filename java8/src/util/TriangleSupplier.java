package util;

import java.util.function.IntSupplier;
import java.util.function.LongSupplier;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

/**
 * Supplier for Triangle numbers in sequence.
 *
 * Created by gcharles on 2/12/17.
 */
public class TriangleSupplier implements IntSupplier {
    private int value = 0;
    private int count = 0;

    @Override
    public int getAsInt() {
        value += ++count;
        return value;
    }
}
