/**
 * Created by gcharles on 4/7/16.
 */
/**
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/
function euler004() {
   Number.prototype.isPalindrome = function() {
      let s = this.toString();
      let len = s.length;

      for (let i = 0; i < len / 2; i++) {
         if (s.charAt(i) !== s.charAt(len - i - 1)) {
            return false;
         }
      }

      return true;
   };

   let palindrome = 0;
   let yFactor = 101;
   let tests = 0;

   for (let x = 999; x >= 101; x--) {
      for (let y = x; y >= yFactor; y--) {
         let prod = x * y;
         if (prod <= palindrome) {
            break;
         }

         tests++;
         if (prod.isPalindrome()) {
            palindrome = prod;
            yFactor = y;
            break;
         }
      }
   }

   return [palindrome, "Total tests " + tests];
}
