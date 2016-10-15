/**
 * Created by gcharles on 10/10/16.
 */
/**
 * For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even
 * though the rules allow some numbers to be expressed in more than one way there is always a "best" way of
 * writing a particular number.

 For example, it would appear that there are at least six ways of writing the number sixteen:

 IIIIIIIIIIIIIIII
 VIIIIIIIIIII
 VVIIIIII
 XIIIIII
 VVVI
 XVI

 However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most
 efficient, as it uses the least number of numerals.

 The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written
 in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for
 this problem.

 Find the number of characters saved by writing each of these in their minimal form.

 Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
 */
var euler089 = function () {

    return new EulerProblem({
        problem: 89,
        testInput: null, //'p089_roman_test.txt',
        testOutput: 4,
        realInput: 'p089_roman.txt',
        realOutput: 743,

        solver: function(filePath) {
            function computeDifference(romanNumeral) {
                let origLength = romanNumeral.length;
                let val = RomanNumeral.parse(romanNumeral);
                return origLength - RomanNumeral.format(val).length;
            }

            let text = readEulerDataFile(filePath);
            let romanNumerals = text.split('\n').filter(line => line.trim().length > 0).map(line => line.trim());

            return romanNumerals.reduce((sum, rn) => sum + computeDifference(rn), 0);
        }
    });

}();
