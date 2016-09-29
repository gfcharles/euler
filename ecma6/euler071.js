/**
 * Created by gcharles on 9/6/16.
 */
/**
 Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

 If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

 It can be seen that 2/5 is the fraction immediately to the left of 3/7.

 By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
 */
var euler071 = new EulerProblem({
    problem: 71,
    testInput: 8,
    testOutput: 2,
    realInput: 1000000,
    realOutput: 428570,

    solver: function (n) {
        const target = 3.0 / 7.0;

        let results = {quotient: 0};

        for (let d = 3; d <= n; d++) {
            let n = Math.floor(target * d);

            if (d % 7 == 0 && n % 3 == 0) {
                n -= 1;
            }

            let q = n / d;
            if (q > results.quotient && gregmath.gcf(n, d) == 1) {
                results = {numerator: n, quotient: q};
            }
        }

        return results.numerator;
    }
});
