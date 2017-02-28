#!/opt/local/bin/ruby1.9
require 'mathn'

class String
  def anagram?(other)
    return false if other == nil || self.length != other.length
    return other.each_char.to_a.sort == self.each_char.to_a.sort
  end
end


def anagrams?(number, maxFactor)
  numString = number.to_s
  (2..maxFactor).each {|n| return false if !numString.anagram?((n*number).to_s)}
  true
end

def findFirstAnagramNumber(maxFactor)
  return nil if maxFactor < 2
  digitCount = maxFactor
  while (digitCount <= 10) do
    limit = (10**digitCount / maxFactor).to_i
    ('0'..'9').to_a.permutation(digitCount) do |perm| 
      next if perm[0] == '0'
      value = perm.join.to_i
      break if value > limit
      return value if (anagrams?(value, maxFactor))
    end
    digitCount += 1
  end
end

puts findFirstAnagramNumber(6)

puts 1.0 / 7.0
