#!/usr/bin/ruby
sum = 0
File.open("numbers.dat", "r") do |infile|
  while (line = infile.gets)
    sum += line.to_i
  end
end

puts sum.to_s[0,10]
