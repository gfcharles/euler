let RomanNumeral = new function() {
    let parse = function(s) {
        let val = 0;

        for (let count = 0; count < s.length; ++count) {
            let c = s[count];
            let c2 = s[count+1];

            switch (c) {
                case 'M':
                    val += 1000;
                    break;
                case 'D':
                    val += 500;
                    break;
                case 'C':
                    if (c2 === 'M') {
                        val += 900;
                        ++count;
                    } else if (c2 === 'D') {
                        val += 400;
                        ++count;
                    } else {
                        val += 100;
                    }
                    break;
                case 'L':
                    val += 50;
                    break;
                case 'X':
                    if (c2 === 'C') {
                        val += 90;
                        ++count;
                    } else if (c2 == 'L') {
                        val += 40;
                        ++count;
                    } else {
                        val += 10;
                    }
                    break;
                case 'V': {
                    val += 5;
                    break;
                }
                case 'I': {
                    if (c2 === 'X') {
                        val += 9;
                        ++count;
                    } else if (c2 === 'V') {
                        val += 4;
                        ++count;
                    } else {
                        val += 1;
                    }
                }
            }
        }
        return val;
    };

    let format = function(val) {
        let s = [];

        let ms = Math.floor(val / 1000);
        for (let i = 0; i < ms; i++) {
            s.push('M');
        }
        val %= 1000;

        if (val >= 900) {
            s.push('CM');
            val -= 900;
        } else if (val >= 500) {
            s.push('D');
            val -= 500;
        } else if (val >= 400) {
            s.push('CD');
            val -= 400;
        }

        let cs = Math.floor(val / 100);
        for (let i = 0; i < cs; i++) {
            s.push('C');
        }
        val %= 100;

        if (val >= 90) {
            s.push('XC');
            val -= 90;
        } else if (val >= 50) {
            s.push('L');
            val -= 50;
        } else if (val >= 40) {
            s.push('XL');
            val -= 40;
        }

        let xs = Math.floor(val / 10);
        for (let i = 0; i < xs; i++) {
            s.push('X');
        }
        val %= 10;

        if (val >= 9) {
            s.push('IX');
            val -= 9;
        } else if (val >= 5) {
            s.push('V');
            val -= 5;
        } else if (val >= 4) {
            s.push('IV');
            val -= 4;
        }

        for (let i = 0; i < val; i++) {
            s.push('I');
        }

        return s.join('');
    };

    return {format: format, parse: parse};
}();