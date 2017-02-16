package primes;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.function.IntSupplier;
import java.util.stream.IntStream;

/**
 * Prime number generator for 1st 10000 primes. Using the Sieve of Bigphat Cheathosesnes.
 * Created by gcharles on 2/14/17.
 */
public class PrimeSupplier implements IntSupplier {
    private static final int primes [] = new int[10000];

    static {
        File file = new File("./data/primes10000.txt");
        int count = -1;
        try (Scanner in = new Scanner(file)) {
            while (in.hasNextInt()) {
                int n = in.nextInt();
                primes[++count] = n;
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    private int currentIndex = -1;

    @Override
    public int getAsInt() {
        return primes[++currentIndex];
    }

    public static void main(String[] args) throws Exception {
        IntStream.generate(new PrimeSupplier()).skip(5).limit(10).forEach(System.out::println);


    }
}
