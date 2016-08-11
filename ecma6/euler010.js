/**
 * Created by gcharles on 4/19/16.
 */
/**
 The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

 Find the sum of all the primes below two million.
*/
function euler010() {
   const threshold = 2000000;

   let sum = 0;
   for (let prime of primes.PrimeGenerator()) {
      if (prime >= threshold) {
         break;
      }
      sum += prime;
   }

   return sum;
}