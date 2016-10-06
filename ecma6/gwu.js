/**
 * Created by gcharles on 9/18/16.
 */
/**
 * wu-like library for working with iterables.
 */
let gwu = function () {
    "use strict";
    function * map (fnc, iterable) {
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

    function * take(n, iterable) {
        let count = 0;
        for (let el of iterable) {
            if (count++ >= n) {
                return;
            }
            yield el;
        }
    }

    function * drop(n, iterable) {
        let count = 0;
        for (let el of iterable) {
            if (count++ >= n) {
                yield el;
            }
        }
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

    return {
        map: map,
        reduce: reduce,
        take: take,
        takeWhile: takeWhile,
        drop: drop,
        filter: filter
    }
}();