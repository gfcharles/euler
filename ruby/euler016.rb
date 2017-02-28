#!/usr/bin/ruby
n = 1000
sum = 0
puts 1 << n
(1 << n).to_s.each_byte {|b| sum += (b - 48)}
puts sum