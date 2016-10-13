/**
 * Created by gcharles on 8/30/16.
 */
/**
 * The following iterative sequence is defined for the set of positive integers:

 n → n/2 (n is even)
 n → 3n + 1 (n is odd)

 Using the rule above and starting with 13, we generate the following sequence:

 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
 It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
 proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

 Which starting number, under one million, produces the longest chain?

 NOTE: Once the chain starts the terms are allowed to go above one million.
 */
var euler014 = function () {

    return new EulerProblem({
        problem: 14,
        testInput: null,
        realInput: 1000000,
        realOutput: 837799,

        solver: function(n) {
            let maxC = 0, maxI = 0;

            for (let i = Math.ceil(n/3); i < n; i++) {
                let c = collatz(i);
                if (c > maxC) {
                    maxC = c;
                    maxI = i;
                }
            }

            return maxI;
        }
    });

    function collatz(n) {
        let count = 1;

        while (n > 1) {
            if (n & 1)  {
                n = 3 * n + 1;
            } else {
                n = n / 2;
            }
            count += 1;
        }
        return count;
    }
}();
