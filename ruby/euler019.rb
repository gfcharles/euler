#!/usr/bin/ruby
require 'date'
puts (Date.new(1901, 1, 1) .. Date.new(2000, 12, 31)).inject(0) {|count,date| (date.mday == 1 && date.wday == 0) ? (count + 1) : count}
