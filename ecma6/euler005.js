/**
   2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 */
var euler005 = new EulerProblem({
   problem: 5,
   testInput: 10,
   realInput: 20,
   solver: function (n) {
      return primes.lcm([...Range(1,n)]);
   }
});