#!/usr/bin/ruby
class Pentagonal
  attr_reader :knownPentagonals
  
  def initialize(limit=100) 
    @knownPentagonals  = [1]  
    generatePentagonals(limit) 
  end 
  
  def generatePentagonals(limit)
    while (@knownPentagonals.last <= limit) do
      nextPentagonal
    end
  end

  def nextPentagonal 
    n = @knownPentagonals.length + 1
    @knownPentagonals << (n * (3*n - 1) / 2)
  end

  def knownPentagonal?(n)
    return false if (n > @knownPentagonals.last)
    return true if (@knownPentagonals.first == n || @knownPentagonals.last == n)

    a, b = 0, @knownPentagonals.length - 1
    while (b - a > 1) do
      m = (a + b) / 2
      return true if @knownPentagonals[m] == n
      (n > @knownPentagonals[m]) ?  a = m : b = m
    end
    
    false
  end
     
  def pentagonal?(n)
    generatePentagonals(n)
    return knownPentagonal?(n)
  end
  
  def pentagonals(limit)
    n = 0
    while true
      while (n >= @knownPentagonals.length) do
        return if @knownPentagonals.last >= limit
        nextPentagonal
      end
      yield n, @knownPentagonals[n]
      n += 1
    end
  end
end

def findDiff
  p = Pentagonal.new()
  p.pentagonals(1_000_000) do |n, pent| 
    (n-1).downto(0) do |i|
      return (pent - p.knownPentagonals[i]) if p.pentagonal?(pent - p.knownPentagonals[i]) && p.pentagonal?(pent + p.knownPentagonals[i])
    end
  end
end

puts findDiff

