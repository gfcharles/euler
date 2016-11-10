/**
 * Created by gcharles on 11/5/16.
 */
describe('Test my_math', function () {
    it('should compute slope and intercept for a line from two points', function () {
        let start = new MyMathUtils.Point(-1, -2);
        let end = new MyMathUtils.Point(2, 7);

        let line = new MyMathUtils.Line({pointA: start, pointB: end});
        expect(line.slope).toBe(3);
        expect(line.intercept).toBe(1);
    });

    it('should compute intersection of line', function () {
        let line1 = new MyMathUtils.Line({slope: 2, intercept: 3});
        let line2 = new MyMathUtils.Line({slope: -0.5, intercept: 7});
        let point = line1.intersection(line2);

        expect(point.x).toBe(1.6);
        expect(point.y).toBe(6.2);
    });
});