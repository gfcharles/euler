/**
 * Created by gcharles on 9/18/16.
 */
/**
 * wu-like library for working with iterables.
 */
let gwu = function () {
    "use strict";
    // Range generator
    function* Range(begin, end, interval = 1) {
        for (let i = begin; i <= end; i += interval) {
            yield i;
        }
    }

    function isIterable (obj) {
        return obj && typeof obj[Symbol.iterator] === 'function';
    };

    function* map (fnc, iterable) {
        for (let el of iterable) {
            yield fnc(el);
        }
    }

    function reduce (fnc, iterable, init) {
        let result = init;
        let first = true;
        for (let el of iterable) {
            if (first) {
                if (typeof(init) === 'undefined') {
                    result = el;
                } else {
                    result = fnc(init, el);
                }
                first = false;
            } else {
                result = fnc(result, el);
            }
        }

        return result;
    }

    function* take(n, iterable) {
        let count = 0;
        for (let el of iterable) {
            if (count++ >= n) {
                return;
            }
            yield el;
        }
    }

    function* drop(n, iterable) {
        let count = 0;
        for (let el of iterable) {
            if (count++ >= n) {
                yield el;
            }
        }
    }

    function nextValue(iterable) {
        return iterable.next().value;
    }

    function * takeWhile(fnc, iterable) {
        for (let el of iterable) {
            if (fnc(el)) {
                yield el;
            } else {
                return;
            }
        }
    }

    function * filter(fnc, iterable) {
        for (let el of iterable) {
            if (fnc(el)) {
                yield el;
            }
        }
    }

    function all(fnc, iterable) {
        for (let el of iterable) {
            if (!fnc(el)) {
                return false;
            }
        }
        return true;
    }

    function any(fnc, iterable) {
        for (let el of iterable) {
            if (fnc(el)) {
                return true;
            }
        }
        return false;
    }

    function count(iterable) {
        let count = 0;
        for (let el of iterable) {
            ++count;
        }
        return count;
    }

    function sum(iterable) {
        return reduce((sum, x) => sum + x, 0);
    }

    function forEach(fnc, iterable) {
        for (let el of iterable) {
            fnc(el);
        }
    }

    return {
        Range: Range,
        map: map,
        reduce: reduce,
        count: count,
        sum: sum,
        take: take,
        takeWhile: takeWhile,
        drop: drop,
        nextValue: nextValue,
        filter: filter,
        all: all,
        any: any,
        forEach: forEach
    }
}();