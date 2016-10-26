/**
 * Created by gcharles on 10/22/16.
 */
/**
 The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
 are themselves prime.

 There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

 How many circular primes are there below one million?
 */
var euler035 = function() {
    let regex = /[024685]/;

    let checkPrime = function () {
        let memo = new Map();

        return function (s) {
            if (memo.has(s)) {
                return memo.get(s);
            }

            let isPrime = primes.checkPrime(Number.parseInt(s));
            memo.set(s, isPrime);

            return isPrime;
        };
    }();

    return new EulerProblem({
        problem: 35,
        testInput: 100,
        testOutput: 13,
        realInput: 1000000,
        realOutput: 55,

        solver: function (n) {
            return gwu.count(
                gwu.filter(s => gwu.all(rotation => checkPrime(rotation), rotations(s)),
                    gwu.filter(s => regexTest(s),
                        gwu.map(n => n.toString(),
                            gwu.takeWhile(p => p < n,
                                primes.PrimeCandidates())))));
        }
    });


    function regexTest(s) {
        if (s === '2' || s === '5') {
            return true;
        }
        return !regex.test(s);
    }

    function* rotations(s) {
        let previous = [];
        for (let i = 0; i != s.length; ++i) {
            let s2 = (i === 0) ? s : s.slice(i) + s.slice(0, i);

            if (previous.indexOf(s2) < 0) {
                previous.push(s2);
                yield s2;
            }
        }
    }

}();

