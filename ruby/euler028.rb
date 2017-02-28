#/usr/bin/ruby
max = 1001
puts (1..max).inject(-3) {|sum, x| x % 2 == 0 ? sum : sum + 4 * x**2 - 6 * x + 6}
  
  
