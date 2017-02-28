require 'mathn'

class String
  def anagram?(other)
    return false if other == nil || self.length != other.length
    return other.each_char.to_a.sort == self.each_char.to_a.sort
  end
end

class Integer
  def anagram?(other, base=10)
    return false if other == nil
    return self.to_s(base).anagram?(other.to_s(base))
  end
end

max = 1_000_000
primes = []
Prime.each {|prime| if prime >  max then break else primes << prime  end }
puts primes.length

primes.reverse!
puts primes.first

#primes.each do |x|
#  n,psi = x * x, x * (x-1)
#  puts n,psi,'-----' if n < 10_000_000 and n.anagram?(psi)
#end

ratio, answer = 2.0, 0

primes.each do |x|
  break if (x.to_f) / (x - 1).to_f > ratio
  primes.each do |y|
    n,phi = x * y, (x - 1) * (y - 1)
    if n < 10_000_000
      break if n.to_f / phi.to_f > ratio
      if n.anagram?(phi)
        puts n,phi,'-----'
        ratio, answer = phi, n
      end
    end
  end
end


puts 8319823.prime_division
puts answer