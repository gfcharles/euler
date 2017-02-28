#!/usr/bin/ruby
class Integer
  def nCr(m)
    return 0 if self < m || self <= 0 || m <= 0

    n, m = self, [self - m, m].max
    result = 1
    self.downto(m+1) {|i| result *= i}
    2.upto(n-m) {|i| result /= i}
    return result
  end
end

puts 40.nCr(20)
