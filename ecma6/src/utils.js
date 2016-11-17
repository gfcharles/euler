/**
 * Created by gcharles on 3/23/16.
 */
function output(message) {
    $(document.body).append('<div>' + message + '</div>');
}

/**
 * The Tiny encryption algorithm
 */
class Tea {
    constructor(key) {
        this.key = key;
        this.delta = 0x9e3779b9;
        /* a key schedule constant */
    }

    encrypt(value) {
        let v0 = value, v1 = Math.floor(Math.random() * 0xFFFFFFFF), sum = 0;
        /* set up */

        for (let i = 0; i < 32; i++) {                       /* basic cycle start */
            sum += this.delta;
            v0 += ((v1 << 4) + this.key[0]) ^ (v1 + sum) ^ ((v1 >> 5) + this.key[1]);
            v1 += ((v0 << 4) + this.key[2]) ^ (v0 + sum) ^ ((v0 >> 5) + this.key[3]);
        }
        /* end cycle */

        return [v0, v1];
    }

    decrypt(cipher) {
        let v0 = cipher[0], v1 = cipher[1], sum = 0xC6EF3720, i;
        /* set up */

        for (i = 0; i < 32; i++) {                         /* basic cycle start */
            v1 -= ((v0 << 4) + this.key[2]) ^ (v0 + sum) ^ ((v0 >> 5) + this.key[3]);
            v0 -= ((v1 << 4) + this.key[0]) ^ (v1 + sum) ^ ((v1 >> 5) + this.key[1]);
            sum -= this.delta;
        }
        /* end cycle */

        return v0;
    }
}