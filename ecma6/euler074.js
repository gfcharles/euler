/**
 * Created by gcharles on 9/21/16.
 */
/**
 * The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

 1! + 4! + 5! = 1 + 24 + 120 = 145

 Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

 169 → 363601 → 1454 → 169
 871 → 45361 → 871
 872 → 45362 → 872

 It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
 78 → 45360 → 871 → 45361 (→ 871)
 540 → 145 (→ 145)

 Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

 How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
 */
var euler074 = function () {
    let factorials = gwu.reduce((ary, d) => {
        ary.push(ary[ary.length - 1] * d);
        return ary;
    }, gwu.Range(1, 9), [1]);

    return new EulerProblem({
        problem: 74,
        testInput: customTest,
        realInput: 1000000,

        solver: function (n) {
            let result = [...gwu.filter(x => sequenceLength(x) === 60, Range(1,n-1))];
            console.log(result);
            return result.length;
        }
    });

    function customTest() {
        return [
            `Test for Problem 74: Sum of digits factorials for 145 is ${sumOfDigitFactorials(145)}`,
            `Test for Problem 74: Sum of digits factorials for 1450 is ${sumOfDigitFactorials(1450)}`,
            `Test for Problem 74: Sequence Length for 69 is ${sequenceLength(69)}`,
            `Test for Problem 74: Sequence Length for 78 is ${sequenceLength(78)}`,
            `Test for Problem 74: Sequence Length for 540 is ${sequenceLength(540)}`,
        ];
    }

    function sequenceLength (n) {
        let length = 0;
        let current = n;
        while (true) {
            length++;
            if ([169, 363601, 1454].includes(current)) {
                return length + 2;
            }
            if ([871, 45361, 872, 45362].includes(current)) {
                return length + 1;
            }

            let next = sumOfDigitFactorials(current);
            if (current === next) {
                return length;
            }

            current = next;
        }
    }

    function sumOfDigitFactorials(n) {
        return gwu.reduce((sum, c) => sum + factorials[c], n.toString(), 0);
    }
}();
