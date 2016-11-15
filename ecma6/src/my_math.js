/**
 * Created by gcharles on 9/5/16.
 */
"use strict";

let MyMathUtils = function () {
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

    // Solve equation ax^2 + bx + c = 0 for x.
    function solveQuadratic(a, b, c) {
        let discriminant = Math.sqrt(b * b - 4 * a * c);

        return [(-b + discriminant) /(2 * a), (-b  - discriminant) / (2 * a)];
    }

    class Point {
        constructor(x, y) {
            this.x = x;
            this.y = y;
        }

        toString() {
            return `Point: (${this.x}, ${this.y})`;
        }
    }

    class Line {
        constructor(options) {
            if (options.slope != null && options.intercept != null) {
                this.slope = options.slope;
                this.intercept = options.intercept;
            } else if (options.slope != null && options.point instanceof Point) {
                this.slope = options.slope;
                this.intercept = options.point.y - options.slope * options.point.x;
            } else if (options.pointA instanceof Point && options.pointB instanceof Point) {
                this.slope = (options.pointA.y - options.pointB.y) / (options.pointA.x - options.pointB.x);
                this.intercept = options.pointA.y - this.slope * options.pointA.x;
            }
        }

        intersection(line) {
            let x = (this.intercept - line.intercept) / (line.slope - this.slope);
            let y = this.slope * x + this.intercept;

            return new Point(x, y);
        }

        reflectionAround(line) {
            let crossingPoint = this.intersection(line);

            let angleIn = Math.atan(this.slope);
            let angleR = Math.atan(line.slope);

            let theta = angleIn - angleR;
            let angleOut = angleIn - 2 * theta;
            let slope =  Math.tan(angleOut);

            return new Line({slope: slope, point: crossingPoint});
        }

        pointAtX(x) {
            let y = this.slope * x + this.intercept;
            return new MyMathUtils.Point(x, y);
        }

        pointAtY(y) {
            let x = (y - this.intercept) / this.slope;
            return new MyMathUtils.Point(x, y);
        }

        toString() {
            return `Line: y = ${this.slope} * x + ${this.intercept}`;
        }
    }

    return {
        combinations: combinations,
        gcf: gcf,
        lcm: lcm,
        solveQuadratic: solveQuadratic,
        Line: Line,
        Point: Point
    }
}();
