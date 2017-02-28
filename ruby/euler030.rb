#!/usr/bin/ruby
def sum_of_digits?(n, power)
  n == n.to_s.split(//).inject(0) {|sum, digit| sum += (digit.to_i ** power) }
end

def get_upper_bound(power) 
  base = 9 ** power
  digit_count = 2
  upper_bound = 0
  while (digit_count += 1) do 
    return upper_bound if ((digit_count * base).to_s).length < digit_count
    upper_bound = digit_count * base
  end
end

puts (10..get_upper_bound(5)).select {|n| sum_of_digits?(n, 5)}.inject {|sum, x| sum + x}
