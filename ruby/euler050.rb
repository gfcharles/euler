#!/opt/local/bin/ruby1.9
require 'mathn'

def findLongestSequencePrime(max = 1_000_000)
  sum, primes = 0,[]
  Prime.each {|prime| if sum + prime >  max then break else sum += prime; primes << prime  end }
  
  sums = [sum]
  (0...primes.length).each do |level|
    nextLevel = []
    sums.each_with_index do |sum, position|
      return sum if sum.prime?
      nextLevel << sum - primes[level-position]
    end
    nextLevel << sums.last - primes[-level-1]
    sums = nextLevel 
  end
end

puts findLongestSequencePrime(1_000_000_000_000)

