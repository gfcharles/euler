/**
 * Created by gcharles on 4/19/16.
 */
/**
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
                                                                           a^2 + b^2 = c^2

   For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/
var euler009 = new EulerProblem({
   problem: 9,
   testInput: 3 + 4 + 5,
   testOutput: 3 * 4 * 5,
   realInput: 1000,
   realOutput: 31875000,

   solver: function (n) {
      for (let a = 1; a < n; a++) {
         for (let b = a + 1; b < n - a; b++) {
            let c = n - a - b;
            if (a * a + b * b === c * c) {
               return a * b * c;
            }
         }
      }

      return Number.NaN;
   }
});