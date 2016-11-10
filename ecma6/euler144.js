/**
 In laser physics, a "white cell" is a mirror system that acts as a delay line for the laser beam. The beam enters
 the cell, bounces around on the mirrors, and eventually works its way back out.

 The specific white cell we will be considering is an ellipse with the equation 4x2 + y2 = 100

 The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing, allowing the light to enter and exit
 through the hole.


 The light beam in this problem starts at the point (0.0,10.1) just outside the white cell, and the beam
 first impacts the mirror at (1.4,-9.6).

 Each time the laser beam hits the surface of the ellipse, it follows the usual law of reflection
 "angle of incidence equals angle of reflection." That is, both the incident and reflected beams make
 the same angle with the normal line at the point of incidence.

 In the figure on the left, the red line shows the first two points of contact between the laser beam and
 the wall of the white cell; the blue line shows the line tangent to the ellipse at the point of incidence
 of the first bounce.

 The slope m of the tangent line at any point (x,y) of the given ellipse is: m = −4x/y

 The normal line is perpendicular to this tangent line at the point of incidence.

 The animation on the right shows the first 10 reflections of the beam.

 How many times does the beam hit the internal surface of the white cell before exiting?

 * Created by gcharles on 11/4/16.
 */
var euler144 = function() {
    return new EulerProblem({
        problem: 144,
        realInput: {p0: {x: 0.0, y: 10.1}, p1: {x: 1.4, y: -9.6}},
        realOutput: 354,

        solver: function (n) {
            let start = new MyMathUtils.Point(n.p0.x, n.p0.y);
            let end = new MyMathUtils.Point(n.p1.x, n.p1.y);
            let rayIn = new MyMathUtils.Line({pointA: start, pointB: end});

            let count = 0;
            while ( !testEscape( end ) ) {
                let tangent  = tangentSlope( end );
                let reflectionLine = new MyMathUtils.Line({ slope: -1 / tangent, point: end });
                let rayOut = rayIn.reflectionAround(reflectionLine);

                let currentX = end.x;
                start = end;
                end = computeNextReflectionPoint(rayOut, currentX);
                rayIn = rayOut;
                ++count;
                //console.log(end.toString());
            }
            return count;
        }
    });

    // Returns slope to tangent of ellipse at point p. Tangent dy/dx (y = 100 - 4x^2) =
    // -4x / sqrt(100 - 4x^2) = -4x / y.
    // Assume tangent can't be 0 or infinite.
    function tangentSlope(p) {
        return -4.0 * p.x / p.y;
    }

    // Solve for intersection of line y = mx + b with ellipse 4x^2 + y^2 = 100.
    // 4x^2 + y^2 = 100
    // 4x^2 + (mx + b)^2 = 100
    // (4 + m^2) * x2 + (2 * m * b) * x + (b * b - 100) = 0
    function computeNextReflectionPoint(ray, currentX) {
        let a = 4 + ray.slope * ray.slope;
        let b = 2 * ray.slope * ray.intercept;
        let c = ray.intercept * ray.intercept - 100;

        // Two solutions should be the x of the point we want and the x of the point we have.
        let solutions = MyMathUtils.solveQuadratic(a, b, c);

        // Sanity check. Make sure one of the solutions matches the point we already have.
        let diffs = solutions.map(x => Math.abs(x - currentX));
        if (Math.min.apply(null, diffs) > 1e-8) {
            throw new Error("current point not in solution");
        }

        // Find the solution for the point we don't already have
        let newX = (diffs[0] > diffs[1]) ? solutions[0] : solutions[1];

        return ray.pointAtX(newX)
    }

    // Escape condition for a ray.
    function testEscape(p) {
        return p.y > 0 && p.x >= -0.01 && p.x <= 0.01;
    }
}();