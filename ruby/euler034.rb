#!/usr/bin/ruby
def factorialList(n)
    (2..n).inject([1,1]) {|list, i| list << i * list.last}
end
  
def sum_of_digits?(n, factorials)
  n == n.to_s.split(//).inject(0) {|sum, digit| sum += factorials[digit.to_i] }
end

def get_upper_bound(nineFactorial) 
  base = nineFactorial
  digit_count = 2
  upper_bound = 0
  while (digit_count += 1) do 
    return upper_bound if ((digit_count * base).to_s).length < digit_count
    upper_bound = digit_count * base
  end
end

f = factorialList(9)
puts (10..get_upper_bound(f[9])).select {|n| sum_of_digits?(n, f)}.inject {|sum, x| sum + x}
