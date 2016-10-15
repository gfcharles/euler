/**
 * Created by gcharles on 9/6/16.
 */
/**
 2<sup>15</sup> = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

 What is the sum of the digits of the number 2<sup>1000<sup>?
 */
function euler016(exp = 1000) {

    class BigInteger {
        constructor(initValue) {
            this.digits = [...initValue.toString(10)].reverse().map(d => parseInt(d));
        }

        toString() {
            this.digits.reverse();
            let s = this.digits.join('');
            this.digits.reverse();
            return s;
        }

        double() {
            let carry = 0;

            for (let i = 0; i < this.digits.length; i++) {
                this.digits[i] = 2 * this.digits[i] + carry;

                if (this.digits[i] >= 10) {
                    this.digits[i] -= 10;
                    carry = 1;
                } else {
                    carry = 0;
                }
            }

            if (carry) {
                this.digits[this.digits.length] = 1;
            }

            return this;
        }

        sumOfDigits() {
            return this.digits.reduce((sum, x) => sum + x);
        }
    }

    let value = new BigInteger(1);


    for(let i = 0; i < exp; i++) {
        value = value.double();
    }

    return value.sumOfDigits();
}