/**
 * Created by gcharles on 4/15/16.
 */
/**
 *
 *
 *  The sum of the squares of the first ten natural numbers is,
 *  12 + 22 + ... + 102 = 385
 *
 *  The square of the sum of the first ten natural numbers is,
 *  (1 + 2 + ... + 10)2 = 552 = 3025
 *
 *  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
 *
 *  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
 *
 */
let euler006 = {
   problem: 6,
   testInput: 10,
   realInput: 100,

   solvers: {
      math: function (n) {
         return Math.pow((n * (n + 1)) / 2, 2) - (n * (n + 1) * (2 * n + 1) / 6);
      },

      bruteForce: function (n) {
         let sumOfSquares = 0;
         let sum = 0;

         for (let i of Range(1, n)) {
            sum += i;
            sumOfSquares += (i * i);
         }

         return sum * sum - sumOfSquares;
      }
   }
};