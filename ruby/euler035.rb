#!/usr/bin/ruby
require 'Primes.rb'

class Integer
  def rotate(pos = 1)
    string = self.to_s
    pos = pos % string.length
    return self if pos == 0
    (string[-pos..-1] + string[0..-pos-1]).to_i
  end
  
  def rotations
    (1..self.to_s.length).inject([]) {|list, pos| list << self.rotate(pos)}.uniq
  end
end

class Primes
  def litmus?(n)
    return true if n == 2 
    n.to_s.index(/[024685]/) == nil
  end 
  
  def rotationalPrime?(n)
    return false if !litmus?(n)
    n.rotations.each {|x| return false if !prime?(x)}
    true
  end
end

p = Primes.new(1_000_000)
puts p.knownPrimes.select {|n| p.rotationalPrime?(n)}.length
