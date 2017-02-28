#!/opt/local/bin/ruby1.9
require 'mathn'
def findSmallestOfEightPrimes
  Prime.each do |prime|
    next if prime <= 56003  # Given in problem statement
    match = prime.to_s.match(/([012])\d*\1\d*\1\d/)
    next if match == nil
    misses = match[1].to_i
    nextDigit = misses + 1
    while nextDigit <= 9 && misses <= 2
      misses += 1 if !prime.to_s.tr(match[1], nextDigit.to_s).to_i.prime?
      nextDigit += 1
    end
    return prime if misses <= 2
  end
end

puts findSmallestOfEightPrimes
