#!/usr/bin/ruby
class Generator
  attr_reader :knownPentagonal
  
  def initialize(method, limit=100) 
    @method = method
    @known = [1]  
    generate(limit) 
  end 
  
  def generate(limit)
    while (@known.last <= limit) do
      nextMember
    end
  end

  def nextMember 
    n = @known.length + 1
    @known << @method.call(n)
  end

  def known?(n)
    return false if (n > @known.last)
    return true if (@known.first == n || @known.last == n)

    a, b = 0, @known.length - 1
    while (b - a > 1) do
      m = (a + b) / 2
      return true if @known[m] == n
      (n > @known[m]) ?  a = m : b = m
    end
    
    false
  end
     
  def member?(n)
    generate(n)
    known?(n)
  end
  
  def members(limit)
    n = 0
    while true
      while (n >= @known.length) do
        return if @known.last >= limit
        nextMember
      end
      yield n, @known[n]
      n += 1
    end
  end
end

def findHexPentTriNumber
  t = Generator.new(lambda {|n| n * (n + 1) / 2 })
  p = Generator.new(lambda {|n| n * (3 * n - 1) / 2 })
  h = Generator.new(lambda {|n| n * (2 * n - 1) })
  h.members(10_000_000_000) {|n, member| return member if member > 40755 && p.member?(member) && t.member?(member) }
end

puts findHexPentTriNumber
