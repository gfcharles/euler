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

total = 0
(2...10000).each do |val| 
  sum = properFactors(val).sum
  if (sum > val && properFactors(sum).sum == val)
    print "#{val} and #{sum}\n"
    total += (val + sum)
  end
end
print "Total = #{total}\n"
   


