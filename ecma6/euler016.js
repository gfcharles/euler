/**
 * Created by gcharles on 9/6/16.
 */
/**
 2<sup>15</sup> = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

 What is the sum of the digits of the number 2<sup>1000<sup>?
 */
var euler016 = function () {

    class BigInteger {
        constructor() {
            this.digits = [1];
        }

        /**
         * Doubles the internal value, kept as an array of decimal digits from least to most significant.
         */
        double() {
            let carry = 0;

            for (let i = 0; i < this.digits.length; i++) {
                this.digits[i] = 2 * this.digits[i] + carry;
                carry = 0;

                if (this.digits[i] >= 10) {
                    this.digits[i] -= 10;
                    carry = 1;
                }
            }

            if (carry) {
                this.digits.push(carry);
            }
        }
    }

    return new EulerProblem({
        problem: 16,
        testInput: 15,
        testOutput: 26,
        realInput: 1000,
        realOutput: 1366,

        solver: function(n) {
            let value = new BigInteger();

            for(let i = 0; i < n; i++) {
                value.double();
            }

            return value.digits.reduce((sum, x) => sum + x);
        }
    });
}();