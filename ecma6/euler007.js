/**
 * Created by gcharles on 4/15/16.
 */
/**
 *  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 *
 *  What is the 10 001st prime number?
 */
function euler007() {
   return primes.PrimeGenerator(10001).next().value;
}
