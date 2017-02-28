#!/usr/bin/ruby
def digit(position)
  remainder = position - 1
  n = 0
  while (remainder > ((n+1) * 9 * 10**n)) do
    remainder -= ((n+1) * 9 * 10**n)
    n += 1
  end
  number = (remainder/(n+1)) + 10**n
  digit = number.to_s[remainder % (n+1)].to_i
end

puts digit(1) * digit(10) * digit(100) * digit(1_000) * digit(10_000) * digit(100_000) * digit(1_000_000)  
