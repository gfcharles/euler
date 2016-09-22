/**
 * Created by gcharles on 3/23/16.
 */
class EulerProblem {
    constructor(def) {
        this.def = def;
        if (!def.solver && def.solvers) {
            let allKeys = Object.keys(def.solvers);
            if (allKeys.length > 0) {
                this.def.solver = def.solvers[allKeys[0]];
            }
        }
    }

    solveSingle(n) {
        if (typeof(n) === 'undefined' && this.def.realInput === null) {
            return `Problem ${this.def.problem} has no input defined`;
        }

        let timer = new FunctionTimer();
        timer.start();
        let value = this.def.solver(n || this.def.realInput);
        timer.stop();

        return new EulerSolution(this.def.problem, value, timer.toString(), n);
    }

    solve(n) {
        if (typeof(n) === 'undefined' && this.def.realInput === null) {
            return [`Problem ${this.def.problem} has no input defined`];
        }

        if (this.def.solvers) {
            return Object.keys(this.def.solvers).map((method) => {
                let timer = new FunctionTimer();
                timer.start();
                let value = this.def.solvers[method](n || this.def.realInput);
                timer.stop();

                return new EulerSolution(this.def.problem, value, timer.toString(), n, method);
            });
        } else {
            return [this.solveSingle(n)];
        }
    }

    test() {
        if (this.def.testInput === null) {
            return [`Problem ${this.def.problem} has no test input defined`];
        }

        if (typeof this.def.testInput === 'function') {
            return this.def.testInput();
        } else {
            return this.solve(this.def.testInput);
        }
    }
}

class EulerSolution {
    constructor(problem, value, timeTaken, input, method = null) {
        this.problem = problem;
        this.value = value;
        this.timeTaken = timeTaken;
        this.input = input;
        this.method = method;
    }

    toString() {
        let s = `Result for problem ${this.problem} is ${this.value}`;
        if (this.input) {
            s += ` for input ${this.input}`;
        }
        if (this.timeTaken) {
            s += ` (${this.timeTaken})`;
        }
        if (this.method) {
            s += ` (using ${this.method} method)`
        }

        return s;
    }
}

function outputResults(results) {
    results.forEach(r => output(r));
}

function output(message) {
    $(document.body).append('<div>' + message + '</div>');
}

function outputResult(problem, result) {
    output(`Result for problem ${problem} is <b>${result}</b>`);
}

// Range generator
function* Range(begin, end, interval = 1) {
    for (let i = begin; i <= end; i += interval) {
        yield i;
    }
}

Object.prototype.isIterable = function () {
    return typeof this[Symbol.iterator] === 'function';
};

class FunctionTimer {
    constructor() {
        this.startTime = 0;
        this.totalTime = 0;
        this.started = false;
    }

    start() {
        if (this.started) {
            throw 'Timer already started';
        }
        this.started = true;
        this.totalTime = 0;
        this.startTime = new Date().getTime();
    }

    stop() {
        if (!this.started) {
            throw 'Timer not started';
        }
        this.started = false;
        this.totalTime = new Date().getTime() - this.startTime;
        this.startTime = 0;
        return this.totalTime;
    }

    toString() {
        return this.totalTime + ' ms'
    }
}
