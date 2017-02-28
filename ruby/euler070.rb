#  Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of
#  positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8,
#  are all less than nine and relatively prime to nine, φ(9)=6.
#
#  The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
#
#  Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
#
#  Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

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

def totient(n, primes, ratio = 2.0)
  isPrime = true
  orig, num, den = n,1,1

  primes.each do |prime|
    break if prime * prime > n

    if n % prime == 0
      isPrime = false
      num,den =  num * (prime - 1), den * prime
      return false, 0, 0.0 if den > ratio * num
      isPrime = false
      while n % prime == 0
        n = n / prime
      end
    end
  end

  if n > 1
    num, den = num * (n-1), den * n
  end
  primes << n if isPrime

  return true, num * (orig / den), den.to_f / num.to_f
end

primes = [3,5,7]
ratio, answer = 2.0, 0

(11..10000000).step(2) do |n|
  valid, psi, newRatio = totient(n, primes, ratio)
  if valid and n.anagram?(psi) and newRatio < ratio
    puts n,psi,ratio
    ratio, answer = newRatio, n
  end
end

puts "answer: :", answer