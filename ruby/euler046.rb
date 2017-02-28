#!/usr/bin/ruby
require 'Primes.rb'

def sumOfTwiceSquarePlusPrime?(n, p)
  limit = ((0.5 * n) ** 0.5).floor
  limit.downto(1) { |x| return true if p.prime?(n -  2 * x**2) }
  false
end

p = Primes.new
n = 1
while (n += 2) do
  break if !p.prime?(n) && !sumOfTwiceSquarePlusPrime?(n,p)
end

puts n
