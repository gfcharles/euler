/**
 * Created by gcharles on 9/9/16.
 */
/**
 * Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

 If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

 It can be seen that there are 21 elements in this set.

 How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
 */
var euler072= new EulerProblem({
    problem: 72,
    testInput: 8,
    realInput: 1000000,

    solver: function (n) {

        let count = 0;
        for (let d = 2; d <= n; d++) {
            let factors = primes.primeFactors(d).factors();
            if (factors.length == 1) {
                count += (d - 1);
            } else {
                count += [...factors].reduce((n, x) => n - n / x, d);
            }
        }

        return count;
    }
});
