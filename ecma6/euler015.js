/**
 * Created by gcharles on 10/14/16.
 */
/**
 * Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are
 * exactly 6 routes to the bottom right corner.
 *
 * How many such routes are there through a 20×20 grid?
 * @type {EulerProblem}
 */
var euler015 = new EulerProblem({
    problem: 15,
    testInput: {rows: 2, columns: 2, toString: function () {return `${this.rows} x ${this.columns}`;}},
    testOutput: 6,
    realInput: {rows: 20, columns: 20},
    realOutput: 137846528820,

    solver: function(n) {
        let totalMoves = n.rows + n.columns;
        let horizontalMoves = n.columns;

        return MyMathUtils.combinations(totalMoves, horizontalMoves);
    }
});
