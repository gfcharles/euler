/**
 * Created by gcharles on 9/5/16.
 */
"use strict";

let gregmath = function () {
    function combinations(n, m) {
        let k = Math.min(m, n-m);
        let prod = 1;
        for (let i = 0; i < k; i++) {
            prod = prod * (n - i) / (i + 1);
        }

        return prod;
    }

    function gcf(a, b) {
        while (b > 0) {
            if (a > b) {
                // [a, b] = [b, a];
                let temp = a;
                a = b;
                b = temp;
            }
            b = b % a;
        }

        return a;
    }

    function lcm(a, b) {
        return a / gcf(a,b) * b;
    }

    return {
        combinations: combinations,
        gcf: gcf,
        lcm: lcm
    }
}();
