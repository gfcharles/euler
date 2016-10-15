/**
 * Created by gcharles on 10/4/16.
 */
/**
 A number chain is created by continuously adding the square of the digits in a number to form a new number until
 it has been seen before.

 For example,

 44 → 32 → 13 → 10 → 1 → 1
 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

 Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY
 starting number will eventually arrive at 1 or 89.

 How many starting numbers below ten million will arrive at 89?
 */
/**
 * Created by gcharles on 4/19/16.
 */
var euler092 = function () {
    let known = [];

    for (let i of [1,44,32,13,10]) {
        known[i] = false;
    }
    for (let i of [89,85,145,42,20,4,16,37,58]) {
        known[i] = true;
    }

    let digitSquares = [...gwu.map(x => x * x, gwu.Range(0,9))];

    return new EulerProblem({
        problem: 92,
        testInput: null,
        realInput: 10000000,
        realOutput: 8581146,

        solver: function(n) {
            let maxToStore = Math.ceil(Math.log(n) / Math.log(10) * digitSquares[9]);
            return gwu.reduce((sum, x) => endsIn89(x, maxToStore) ? sum + 1 : sum, gwu.Range(1,n-1), 0);
        }
    });


    function endsIn89(num, max) {
        if (known[num] === true) {
            return true;
        } else if (known[num] !== false) {
            let loop = (num <= max) ? [num] : [];
            let end89 = null;

            let next = num;
            while (true) {
                next = computeNextInSequence(next);
                if (known[next] === true || known[next] == false) {
                    end89 = known[next];
                    break;
                }
                loop.push(next);
            }
            for (let m of loop) {
                known[m] = end89;
            }
            return end89;
        }
    }

    function computeNextInSequence(current) {
        return gwu.reduce((sum, c) => sum + digitSquares[c], current.toString(), 0);
    }
}();
