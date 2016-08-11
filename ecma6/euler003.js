/**
 * Created by gcharles on 3/23/16.
 */
//
//  The prime factors of 13195 are 5, 7, 13 and 29.
//
//  What is the largest prime factor of the number 600851475143 ?
//
function euler003() {


   let number = 600851475143;
   let gen = primes.primeGenerator();
   let possibleFactors = [];

   for (let prime = gen.next().value; prime * prime <= number; prime = gen.next().value) {
      possibleFactors.push(prime);
   }

   for (let i = possibleFactors.length -1; i >= 0; i--) {
      if (number % possibleFactors[i] == 0) {
         return possibleFactors[i];
      }
   }
}