#!/usr/bin/ruby
class Permutation
  attr_accessor :elements
  
  def factorialList(n)
    (2..n).inject([1]) {|list, i| list << i * list.last}
  end
  
  def initialize(elements)
    @length = elements.length
    @factorials = factorialList(@length - 1)
    @elements = elements.sort
  end
  
  def getPosition(position)
    elements = @elements.dup
    remainder = position - 1
    answer = ''
    
    1.upto(@length-1) do |x|
      nextIndex = remainder / @factorials[-x]
      answer += elements.slice!(nextIndex).to_s
      remainder -=  (nextIndex * @factorials[-x])
    end
    
    answer + elements[0].to_s
  end  
end


puts Permutation.new((0..9).to_a).getPosition(1_000_000)

