/**
 * Created by gcharles on 3/23/16.
 */
//
//  The prime factors of 13195 are 5, 7, 13 and 29.
//
//  What is the largest prime factor of the number 600851475143 ?
//
function euler003() {
   const number = 600851475143;

   let factorMap = primes.primeFactors(number);
   return Math.max.apply(null, [...factorMap.factors()]);
}