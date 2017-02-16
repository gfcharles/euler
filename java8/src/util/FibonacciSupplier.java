package util;

import java.util.Optional;
import java.util.function.LongPredicate;
import java.util.function.LongSupplier;
import java.util.stream.LongStream;

/**
 * Supplier for FibonacciSupplier numbers in sequence.
 *
 * Created by gcharles on 2/12/17.
 */
public class FibonacciSupplier implements LongSupplier {
    private long a;
    private long b;

    public FibonacciSupplier(long f0, long f1) {
        this.a = f0;
        this.b = f1;
    }

    @Override
    public long getAsLong() {
        long result = a;
        long next = a + b;
        a = b;
        b = next;
        return result;
    }

    public static void main(String[] args) {
        FibonacciSupplier fib = new FibonacciSupplier(1, 2);
        LongStream.generate(fib).limit(1000).forEach(System.out::println);
    }
}
