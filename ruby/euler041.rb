#!/usr/bin/ruby
require "Primes.rb"

class Integer
  def pandigital?
    string = self.to_s
    return false if string.index('0') != nil
    (1..string.length).each {|digit| return false if string.index(digit.to_s) == nil}
    true
  end
end

def maxPrimePandigital()
  p = Primes.new()
  pandigital = '987654321'
  9.downto(1).each do |n|
    slice = []
    (0..n-1).each {|i| slice[i] = pandigital[9-n+i]}
    slice.permutation(n) {|perm| return perm.join if p.prime?(perm.join.to_i)}
  end
end

puts maxPrimePandigital

def demonstrateBug
  n = 3
  slice = '987654321'.chars.to_a[-n..-1]
  puts "slice = #{slice.join}"
  slice.permutation(n) {|perm| puts perm.join}
  
  slice2 = slice.dup
  puts "slice2 = #{slice2.join}"
  slice2.permutation(n) {|perm| puts perm.join}
  
  slice3 = []
  (0...n).each {|i| slice3[i] = slice[i]}
  puts "slice3 = #{slice3.join}"
  slice3.permutation(n) {|perm| puts perm.join}
  
end

demonstrateBug

