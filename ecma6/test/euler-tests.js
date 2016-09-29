/**
 * Created by gcharles on 9/25/16.
 */
function _Fn(ep){
    describe(`Euler Problem ${ep.def.problem} validator`, function () {
        if (ep.def.testInput) {
            for (let testResults of ep.test()) {
                describe('Checks with test input', function () {
                    it('should return correct solution for test input', function () {
                        console.log(testResults.toString());
                        if (testResults instanceof EulerSolution) {
                            expect(testResults.value).toBe(ep.def.testOutput);
                        } else {
                            expect(testResults.toString()).toBe(ep.def.testOutput);
                        }
                    });
                });
            }
        }


        describe('Checks real input', function () {
            let solutions = ep.solve();

            it('should have at least one solution', function () {
                expect(solutions.length).toBeGreaterThanOrEqual(1);
            });

            for (let solution of solutions) {
                it('should return correct solution for real input', function () {
                    console.log(solution.toString());
                    expect(solution.value).toBe(ep.def.realOutput);
                    expect(solution.timeTaken).toBeLessThan(60000);
                });
            }
        });
    });
}


const maxProb = 571;

for (let p = 1; p <= maxProb; p++) {
    let prob = window["euler" + ("00" + p).slice (-3)];
    if (prob instanceof EulerProblem) {
        _Fn(prob);
    }
}
