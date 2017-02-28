#!/usr/bin/ruby
puts (1..100).inject {|x,y| x * y}.to_s.split(//).inject(0) {|a,b| a + b.to_i}