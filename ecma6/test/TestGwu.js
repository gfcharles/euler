describe('Test gwu', function () {
    it('should sum a gwu.Range with no start value', function () {
        expect(gwu.reduce((sum, x) => sum + x, gwu.Range(1, 5))).toBe(15);
    });
    it ('should sum a gwu.Range with given start value', function () {
        expect(gwu.reduce((sum,x) => sum + x, gwu.Range(1,5), 10)).toBe(25);
    });

    it('should sum an Array', function () {
        expect(gwu.reduce((sum, x) => sum + x,[1,2,3,4,5])).toBe(15);
    });

    it('should map a gwu.Range', function () {
        let map = [...gwu.map(x => x * x, gwu.Range(1,5))];
        expect(compareArrays(map, [1,4,9,16,25])).toBe('equal');
    });

    it('should filter a gwu.Range', function () {
        let filter = [...gwu.filter(x => x % 2 == 1, gwu.Range(1,10))];
        expect(compareArrays(filter, [1,3,5,7,9])).toBe('equal');
    });

    it('should map a String', function () {
       let map = [...gwu.map(c => c - '0', '1066')];
        expect(compareArrays(map, [1,0,6,6])).toBe('equal');
    });

// output(gwu.reduce((sum,x) => sum + x, [1,2,3,4,5]));
// output(gwu.reduce((sum,x) => sum + x, [1,2,3,4,5], 99));
// output(gwu.reduce((max,x) => max < x ? x : max, 'AZBYR2D2', 'g'));
//
// output([...gwu.filter(x => x % 2 === 0, gwu.Range(1,10))]);
// output([...gwu.filter(x => x % 2 !== 0, gwu.Range(1,10))]);
// });

});

function compareArrays(a,b) {

    if (a === b) {
        return 'equal';
    }

    if (a.length != b.length) {
        return 'different lengths';
    }

    for (let i = 0; i < a.length; i++) {
        if (a[i] !== b[i]) {
            return `element ${i}: ${a[i]} !== ${b[i]}`;
        }
    }

    return 'equal';
}