#!/usr/bin/ruby
rows = []
count = 0
File.open("euler018.dat", "r") do |infile|
  while (line = infile.gets)
    rows[count] = line.split(' ').map{|x| x.to_i}
    count += 1
  end
end

(rows.length - 1).downto(1) do |row|
  0.upto(rows[row].length-2) do |i|
    rows[row-1][i] += rows[row][i..i+1].max
  end
end

puts rows[0][0]
