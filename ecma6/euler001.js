//
//If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
//Find the sum of all the multiples of 3 or 5 below 1000.
//
function euler001() {
   // Condition done as a fat-arrow function
   let condition = x => x % 3 == 0 || x % 5 == 0;

   // Generator for the range.
   function* range(begin, end, interval = 1) {
      for (let i = begin; i < end; i += interval) {
         yield i;
      }
   }

   return [...range(1,1000)]
      .filter(condition)
      .reduce((sum, x) => sum + x);
}
