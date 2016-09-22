/**
 * Created by gcharles on 4/19/16.
 */
/**
 Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
 If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are
 called amicable numbers.

 For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
 The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

 Evaluate the sum of all the amicable numbers under 10000.
*/
var euler021 = function() {
   return new EulerProblem({
      problem: 21,
      testInput: customTest,
      realInput: 10000,

      solvers: {
         basic: function (n) {
            let sum = 0;
            for (let i = 2; i < n; i++) {
               if (isAmicable(i)) {
                  sum += i;
               }
            }
            return sum;
         },

         'prime factors': function (n) {
            let sum = 0;
            for (let i = 2; i < n; i++) {
               if (isAmicable(i, fmProperDivisors)) {
                  sum += i;
               }
            }
            return sum;
         }
      }
   });

   function properDivisors(n) {
      let divisors = [1];

      for (let i = 2; i * i <= n; i++) {
         if (n % i == 0) {
            divisors.push(i);
            divisors.push(n/i);
         }
      }

      return divisors;
   }

   function fmProperDivisors(n) {
      return new primes.FactorMap(n).properDevisors();
   }

   function sum(ary) {
      return ary.reduce((sum, x) => sum + x, 0);
   }

   function isAmicable(a, f = null) {
      if (!f) {
         f = properDivisors;
      }
      let b = sum(f(a));
      return (a != b) && sum(f(b)) == a;
   }

   function customTest(n) {
      let basic220 = properDivisors(220);
      basic220.sort((a,b) => a - b);
      let fm220 = properDivisors(220);
      fm220.sort((a,b) => a - b);

      return [
         `Test for Problem 21: basic method divisors of 220: ${basic220}, sum ${sum(basic220)}`,
         `Test for Problem 21: fm divisors of 220: ${fm220}, sum ${sum(fm220)}`
      ];
   }
}();
