/**
 * Created by gcharles on 10/11/16.
 */
describe('Test RomanNumeral', function () {
    it('should parse values correctly', function () {
        expect(RomanNumeral.parse('MCMLXVII')).toBe(1967);
        expect(RomanNumeral.parse('IIIIIIIIIIIIIIII')).toBe(16);
        expect(RomanNumeral.parse('VIIIIIIIIIII')).toBe(16);
        expect(RomanNumeral.parse('VVIIIIII')).toBe(16);
        expect(RomanNumeral.parse('XIIIIII')).toBe(16);
        expect(RomanNumeral.parse('VVVI')).toBe(16);
        expect(RomanNumeral.parse('XVI')).toBe(16);
    });

    it('should format values correctly', function () {
        expect(RomanNumeral.format(1967)).toBe('MCMLXVII');
        expect(RomanNumeral.format(16)).toBe('XVI');
        expect(RomanNumeral.format(8978)).toBe('MMMMMMMMCMLXXVIII');
    });

});

