#!/usr/bin/ruby
def computeNameValue(name)
  offset = 'A'[0].to_i - 1
  return name.split(//).inject(0) {|sum, value| sum + value[0].to_i - offset}
end

def readNames(fileName)
  names = []
  File.open(fileName, "r") do |infile|
    names = infile.gets.split(",")
  end

  names.map! {|el| el.tr('"', '')}
  names.sort!
end

total = 0
names = readNames("names.txt")
names.each_with_index { |name, i| total += ((i+1) * computeNameValue(name)) }
puts total
