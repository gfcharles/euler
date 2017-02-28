#!/usr/bin/ruby
require 'Primes.rb'

class Integer
  def truncations() 
    string = self.to_s
    (1..string.length-1).inject([self]) do |truncations, n| 
      truncations << string[0..n-1].to_i 
      truncations << string[-n..-1].to_i
    end.uniq
  end
end

class Primes
  def litmus?(n)
    return true if n == 2 
    string = n.to_s
    string.index(/[0468]/) == nil && string.index(/2/,1) == nil
  end 

  def truncatablePrime?(n)
    return false if (n < 10 || !litmus?(n))
    n.truncations.each {|x| return false if !prime?(x)}
    true
  end
end

list = []
p.primes(100_000_000) {|prime| list << prime if p.truncatablePrime?(prime); break if list.length >= 11 }
puts list.reduce(:+)
