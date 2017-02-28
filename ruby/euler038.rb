#!/usr/bin/ruby
def highestPandigitalProductSum
  "987654321".chars.to_a.permutation do |p| 
    return p.join if p[0..3].join.to_i * 2 == p[4..8].join.to_i
  end
end

puts highestPandigitalProductSum
    
