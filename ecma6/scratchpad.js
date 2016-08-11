/**
 * Created by gcharles on 3/27/16.
 */
Array.prototype.sum = function() {
   return this.reduce((sum, x) => sum + x);
};

Array.prototype.product = function() {
   return this.reduce((prod, x) => prod * x);
};

function testConst() {
   try {
      const a = 4;
      a = 3;
      output('Value of a is ' + a);
   } catch (e) {
      output('Caught exception');
   }

   const b = {name: 'Cheryl', role: 'Secretary'};
   b.name = 'Carol';
   output('Value of b.name is ' + b.name);
}

// function runFactorMap() {
//
//    let fm = new FactorMap();
//    fm.set(2, 4);
//    fm.set(3, 1);
//    output(fm.toString());
//    output(fm.computeValue());
// }
