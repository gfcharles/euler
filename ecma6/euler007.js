/**
 * Created by gcharles on 4/15/16.
 */
/**
 *  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 *
 *  What is the 10 001st prime number?
 */
var euler007 = new EulerProblem({
   problem: 7,
   testInput: 6,
   testOutput: 13,
   realInput: 10001,
   realOutput: 104743,

   solver: function (n) {
      return primes.PrimeGenerator(n).next().value;
   }
});
