#!/usr/bin/ruby
class Primes
  attr_reader :knownPrimes
  
  def initialize(n) 
    @knownPrimes  = [2]  
    generatePrimes(n) 
  end 
  
  def generatePrimes(n)
    #puts "generate to #{n}"
    ((@knownPrimes.last+1)..n).each {|x| @knownPrimes << x if isPrime?(x)}
  end

  def isPrime?(n)
    return false if n < 2
    limit = Math.sqrt(n).floor
    if (limit > @knownPrimes.last) then
      generatePrimes(limit+1)
    end
    
    @knownPrimes.each do |prime|
      return false if (n % prime == 0)
      return true if (prime > limit)
    end
  end
end

max = 0
product = 0

p = Primes.new(1000)
(-1000..1000).each do |a|
  primes = p.knownPrimes
  primes.each do |b|
    n = 1
    while true
      break unless p.isPrime?(n*n + a*n + b)
      n += 1
    end
    if (n-1 > max) then
      max = n-1
      product = a * b
    end
  end
end

puts product
