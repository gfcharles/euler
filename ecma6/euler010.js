/**
 * Created by gcharles on 4/19/16.
 */
/**
 The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

 Find the sum of all the primes below two million.
*/
var euler010 = new EulerProblem({
   problem: 10,
   testInput: 10,
   testOutput: 17,
   realInput: 2000000,
   realOutput: 142913828922,

   solver: function(n) {

      return gwu.reduce((sum, x) => sum + x,
             gwu.takeWhile(p => p < n,
             primes.PrimeGenerator())
      );
   }
});