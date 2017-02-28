#!/usr/bin/ruby
require 'Primes.rb'

class Primes
  def factorList(n) 
    return [n] if self.prime?(n)
    list = []
    @knownPrimes.each { |prime| while (n >= prime && n % prime == 0) do list << prime; n /= prime end }
    list << n if n > 1
    list
  end
end

p = Primes.new
n = 10
count = 0
while (n += 1) do
  distinctFactors =  p.factorList(n).uniq.length
  if distinctFactors == 4 then
    count += 1
  else
    count = 0
  end
  break if count == 4
end

puts n - 3


