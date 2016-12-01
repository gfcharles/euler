/**
 * The square root of 2 can be written as an infinite continued fraction.

 The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum.
 In a similar way, √23 = [4;(1,3,1,8)].

 ...

 It turns out that the sequence of partial values of continued fractions for square roots provide the best
 rational approximations. Let us consider the convergents for √2.

...

 Hence the sequence of the first ten convergents for √2 are:

 1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
 What is most surprising is that the important mathematical constant,
 e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

 The first ten terms in the sequence of convergents for e are:

 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
 The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

 Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
 * Created by gcharles on 11/27/16.
 */
var euler065 = function () {
    return new EulerProblem({
        problem: 65,
        testInput: 10,
        testOutput: 17,
        realInput: 100,
        realOutput: 272,

        solver: function (n) {
            let e  = {base: 2, series: function* () {
                let count = 1;
                while (++count) {
                    yield (count % 3 === 0) ? (2 * Math.floor(count / 3)) : 1;
                }
            }};

            let cfGen = function* (cf) {
                "use strict";
                yield cf.base;
                yield*  cf.series();
            };

            let convergents = function* (cf) {
                "use strict";
                let l = {n: bigInt.zero, d: bigInt.one};
                let r = {n: bigInt.one, d: bigInt.zero};

                function computeNext(x, a, b) {
                    return { n: a.n.add( b.n.multiply( x ) ), d: a.d.add( b.d.multiply( x ) ) };
                }

                for (let x of cfGen(cf)) {
                    l = computeNext(x, l, r);
                    yield l;
                    [l, r] = [r, l];
                }
            };

            let nthConvergent =
                gwu.nextValue(
                    gwu.drop(n - 1,
                        convergents(e)));

            return sumOfDigits(nthConvergent.n);
        }
    });

    function sumOfDigits(n) {
        "use strict";
        return n.toString().split('').reduce((sum, c) => sum + (c - '0'), 0);
    }
}();
