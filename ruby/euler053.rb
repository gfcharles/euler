#!/usr/bin/ruby
class Integer
  def nCr(m)
    return 0 if m <= 0 || self <= 0 || self < m
    m, n = [self - m, m].min, self
    
    (0..(m-1)).inject(1) {|prod, i| prod * (n - i)} / (1..m).reduce(:*)
  end
end

target = 1_000_000
max = 100

count = 0
max.downto(1).each do |n| 
  r = n / 2
  break if n.nCr(r) <= target
  count += (n%2 == 0) ? 1 : 2
  (r - 1).downto(1).each do |m|
    break if n.nCr(m) <= target
    count += 2
  end
end

puts count
