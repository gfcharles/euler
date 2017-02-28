#!/usr/bin/ruby
def computeHypoteneuse(a,b)
  (a.to_f ** 2 + b.to_f ** 2) ** 0.5
end

class Float
  def integer?()
    return (self.round - self).abs < 1e-9
  end
end

max = 1000
sums = []
sums.fill(0,0,max+1)
1.upto(max/2) do |a|
  (a+1).upto(max-a) do |b|  
    c = computeHypoteneuse(a,b)
    break if a+b+c > max 
    sums[a+b+c.round] += 1 if c.integer?
  end
end

puts sums.index(sums.max)
