#!/opt/local/bin/ruby1.9
require 'mathn'
class Integer
  def primePermutations
    digits = self.to_s.each_char.to_a
    list = [] 
    digits.permutation do |perm| 
      next if perm[0] == '0' 
      list << perm.join.to_i if perm.join.to_i.prime?
    end
    list.sort.uniq
  end
  # 
  # def digitsInOrder?(base=10)
  #   true
  #   #self == self.to_s(base).each_char.to_a.sort.join.to_i
  # end
end

class Array
  # find three array members with same difference
  def findTriples
    list = self.sort
    (0...list.length).each do |i|
      (i+1...list.length).each do |j|
        diff = list[j] - list[i]
        k = list.index(list[j]+diff)
        if k != nil then
          return format("%d%d%d", list[i], list[j], list[k])
        end
      end
    end
    nil
  end
end

Prime.each do |n|
  next if n < 1000
  break if n >= 10000

  result = n.primePermutations.findTriples
  if (result != nil && result != '148748178147') then
    puts result
    break
  end
end


