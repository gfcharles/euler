package primes;

import com.protonpack.StreamUtils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.IntSupplier;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * Prime number generator for 1st 10000 primes. Using the Sieve of Bigphat Cheatrosesnes.
 * Created by gcharles on 2/14/17.
 */
public class PrimeSupplier implements IntSupplier {
    private static final List<Integer> primes;

    static {
//        primes = new ArrayList<>(10_000);
//        File file = new File("./data/primes10000.txt");
//        try (Scanner in = new Scanner(file)) {
//            while (in.hasNextInt()) {
//                primes.add( in.nextInt() );
//            }
//        } catch (FileNotFoundException e) {
//            e.printStackTrace();
//        }
        primes = new ArrayList<>(Arrays.asList(2, 3, 5));
    }

    private int currentIndex = 0;

    @Override
    public int getAsInt() {
        while (currentIndex >= primes.size()) {
            primes.add(getNextPrime());
        }

        return primes.get(currentIndex++);
    }

    private int getNextPrime() {
        int lastPrime = primes.get(primes.size() - 1);
        for (int n = lastPrime + 2; ; n += 2) {
            if ($isPrime( n ) ) {
                return n;
            }
        }
    }

    /**
     * Checks if integer is prime.
     *
     * @param n the number to check
     * @return true for prime, false for composite.
     * @throws IllegalArgumentException if n < 2.
     */
    public static boolean isPrime(int n) {
        if (n < 2) {
            throw new IllegalArgumentException("Undefined");
        }

        return n == 2 || n == 3 || $isPrime(n);

    }

    // Check for prime. Assumes n > 3. Otherwise call public
    // method.
    private static boolean $isPrime( int num ) {
        // Fast reject of impossibles.
        if ((num+1) % 6 != 0 && (num-1) % 6 != 0) {
            return false;
        }

        Stream<Integer> infinite = IntStream.generate(new PrimeSupplier()).mapToObj(j -> j);
        IntStream finite = StreamUtils.takeUntil(infinite, j -> j * j > num).mapToInt(j -> j);

        return finite.allMatch(j -> num % j != 0);
    }

    public static Stream<Integer> primeGenerator() {
        return IntStream.generate(new PrimeSupplier()).mapToObj(n -> n);
    }

    public static void main(String[] args) throws Exception {
        IntStream.generate(new PrimeSupplier()).limit(20).forEach(System.out::println);
        //System.out.println($isPrime(3 * 19 * 19 * 19 * 19));
    }
}
