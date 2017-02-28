#!/opt/local/bin/ruby1.9
def hasWeirdProperty?(pandigital)
  divisors = [2,3,5,7,11,13,17]
  (0..6).each {|n| return false if pandigital[n+1..n+3].to_i % divisors[n] != 0}
  true
end

weird = []
"0123456789".chars.to_a.permutation(10) {|perm| weird << perm.join.to_i if hasWeirdProperty?(perm.join)}
puts weird.join(',')
puts weird.length
puts weird.reduce(:+)

#puts hasWeirdProperty?("1406257289")
