#!/usr/bin/ruby
def properFactors(value)
  limit = Math.sqrt(value).floor
  factors = [1]
  (2..limit).each do |x| 
    if value % x == 0 
      factors.push(x)
      y = value / x
      if (y != x)
        factors.push(y)
      end
    end
  end
  factors
end

class Array
   def sum 
     self.inject(0) {|sum, element| sum + element }
   end
end

def isAbundant(value)
   return false if (value <= 1)
   properFactors(value).sum > value
end

max = 28183
abundants =  (0..max).select {|val| isAbundant(val)}

isSumOfTwoAbundants = Array.new(max+1, false)
for i in 0...abundants.length
  for j in i...abundants.length
    sum = abundants[i] + abundants[j]
    if sum > max then
      break
    else 
      isSumOfTwoAbundants[sum] = true
    end
  end
end

puts (1..max).inject(0) {|sum, x| isSumOfTwoAbundants[x] ? sum : sum + x } 

