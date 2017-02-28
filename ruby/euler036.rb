#!/usr/bin/ruby
module Palindrome
  def palindrome?
    string = self.to_s
    string == string.reverse
  end
end

class Integer
  include Palindrome
end

class String
  include Palindrome
end

puts (1..1_000_000).select {|n| n.palindrome? && n.to_s(2).palindrome?}.reduce(:+)
