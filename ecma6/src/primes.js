/**
 * A module for working with prime numbers.
 *
 * @type {{checkPrime, primeGenerator, primeFactors, lcm, gcf}}
 */


let primes = function () {
   // Keep a list of first n known primes.
   let knownPrimes = [2, 3, 5];

   /**
    * Prime number generator function. Can be initialized with a start value, e.g., 5 to start with the 5th prime.
    * Also excepts a start parameter in the next() method to jump to a prime number instead of iterating there.
    * @param start
    */
   let PrimeGenerator = function* (start = 1) {
      let index = Math.max(0, start-1);
      let newIndex;

      while (true) {
         if (newIndex) {
            index = Math.max(0, newIndex-1);
         }
         while (index >= knownPrimes.length) {
            knownPrimes.push(computeNextPrime());
         }
         newIndex = yield knownPrimes[index++];
      }

      function computeNextPrime() {
         for (let i = lastKnownPrime() + 2; ; i += 2) {
            if (checkPrime(i)) {
               // console.log('computed new prime ' + i);
               return i;
            }
         }
      }
   };

   let PrimeCandidates = function* () {
      yield *knownPrimes;

      let mod = lastKnownPrime() % 6;
      let n = ((lastKnownPrime() - mod) / 6) + 1;

      if (mod === 5) {
         yield 6 * n + 1;
         ++n;
      }

      while (true) {
         yield 6 * n - 1;
         yield 6 * n + 1;
         ++n;
      }
   };

   function lastKnownPrime() {
      return knownPrimes[knownPrimes.length - 1];
   }

   /**
    * checkPrime to see if parameter is a prime number
    * @param n
    * @returns {boolean}
    */
   let checkPrime = function (n) {
      // Fast reject of impossibles.
      if (n > 3 && (n+1) % 6 !== 0 && (n-1) % 6 !== 0) {
         return false;
      }

      for (let prime of PrimeGenerator()) {
         if (prime * prime > n) {
            break;
         }
         if (n % prime == 0) {
            return false;
         }
      }

      return true;
   };

   // Class for a map of prime factors. Factors appear as keys in the map, and powers as values.
   // E.g., a factor map of 40 would be {2: 3, 5: 1}.
   class FactorMap extends Map {
      constructor(initValue) {
         super();
         this.factor(initValue);
      }

      factor(n) {
         this.clear();

         if (!n || n < 1) {
            return;
         }

         let residual = n;
         let gen = PrimeGenerator();

         for (let prime of gen) {
            if (prime * prime > residual) {
               break;
            }
            while (residual % prime === 0) {
               this.set(prime, (this.get(prime) || 0) + 1);
               residual /= prime;
            }
         }

         if (residual > 1) {
            this.set(residual, (this.get(residual) || 0) + 1);
         }
      }

      factors() {
         return this.keys();
      }

      exponents() {
         return this.values();
      }

      toString() {
         return [...this.entries()].map(function (kv) {
               if (kv[1] > 1) {
                  return kv.join('^');
               } else {
                  return kv[0];
               }
            }).join(' * ');
      }

      computeValue() {
         return [...this.entries()].map(function (kv) {
            return Math.pow(kv[0], kv[1]);
         }).reduce((prod, x) => prod * x, 1);
      }

      countFactors() {
         return [...this.exponents()].reduce((product, exponent) => product * (exponent + 1), 1);
      }

      properDevisors() {
         let results = [];
         let entries = [...this.entries()];
         let factors = entries.map(a => a[0]);
         let powers = entries.map( a => a[1] + 1 );

         let count = this.countFactors();

         for (let i = 0; i < count - 1; i++) {
            let prod = 1;
            let r = i;

            for(let j = 0; j < factors.length; j++) {
               let f = factors[j];
               let p = r % powers[j];
               prod *= Math.pow(f, p);
               r = ((r - p) / powers[j]);
            }
            results.push(prod);
         }

         return results;
      }

      static _merge(factorMaps, mergeFunction) {
         let merge = new FactorMap();
         let factorsIterator = CombineIterators(factorMaps.map(fm => fm.keys()));
         let factorsSet = new Set(factorsIterator);
         for (let factor of factorsSet) {
            let powers = factorMaps.map(fm => (fm.get(factor) || 0));
            merge.set( factor, mergeFunction( powers ) );
         }
         return merge;
      }

      static lcm(values) {
         let factorMaps = values.map(value => new FactorMap(value));
         let merge = FactorMap._merge(factorMaps, powers => Math.max.apply( Math, powers ) );
         return merge.computeValue();
      }

      static gcf(values) {
         let factorMaps = values.map(value => new FactorMap(value));
         let merge = FactorMap._merge(factorMaps, powers => Math.min.apply( Math, powers ) );
         return merge.computeValue();
      }
   }

   function* CombineIterators(iterators) {
      for (let iter of iterators) {
         yield* iter;
      }
   }

   let primeFactors = function(n) {
      return new FactorMap(n);
   };


   return {
      checkPrime: checkPrime,
      PrimeGenerator: PrimeGenerator,
      PrimeCandidates: PrimeCandidates,
      primeFactors: primeFactors,
      FactorMap: FactorMap,
      lcm: FactorMap.lcm,
      gcf: FactorMap.gcf
   }
}();