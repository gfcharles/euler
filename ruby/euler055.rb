#!/usr/bin/ruby
class Integer
  def reverse(base = 10)
    self.to_s(base).reverse.to_i(base)
  end
  
  def palindrome?(base = 10)
    self.to_s(base).reverse == self.to_s(base)
  end
  
  def lychrel?(maxTries = 50)
    n = self
    maxTries.times do 
      n = n + n.reverse
      return false if n.palindrome?
    end
    
    true
  end
end

puts (1...10000).to_a.select {|n| n.lychrel?}.join(', ')
