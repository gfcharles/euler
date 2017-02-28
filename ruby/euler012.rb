#!/usr/bin/ruby
require 'mathn'

def countTriangleFactors(n, countFactorsMethod)
  if (n % 2 == 0)
    countFactorsMethod.call(n/2) * countFactorsMethod.call(n+1)
  else
    countFactorsMethod.call(n) * countFactorsMethod.call((n+1)/2)
  end
end    

# Straight up counting of factors
def countFactors(value)
  limit = Math.sqrt(value).floor
  factors = 0
  1.upto(limit) {|x| factors += 2 if value % x == 0}
  factors -= 1 if (limit * limit == value)  
  factors
end

# Count factors using some weird list methods.
def countFactors2(value) 
  limit = Math.sqrt(value).floor
  factors = 2 * (1..limit).select {|x| value % x == 0}.length
  factors -= 1 if (limit * limit == value)  
  factors
end

# Count factors weird Ruby way
def countFactors3(value)
  factors = 1
  value.prime_division.each {|factor, count| factors *= (count+1)}
  factors
end

# Compute triangle number of value using injection to create a sum.
def triangle(value) 
   (1..value).inject {|sum, i| sum + i}
end

def runTrial(header, countFactorsMethod) 
  #countFactorsMethod = lambda {|x| countFactors(x) }

  puts header
  
  value = 0
  factors = 0

  beginning = Time.now
  while factors <= 500
    value +=1 
    factors = countTriangleFactors(value, countFactorsMethod)
  end
  puts "Time elapsed #{Time.now - beginning} seconds"

  puts "Triangle number #{triangle(value)} has #{factors} factors."
  puts ""
end

runTrial('Method 1', lambda {|x| countFactors(x) })
runTrial('Method 2', lambda {|x| countFactors2(x)})
runTrial('Method 3', lambda {|x| countFactors3(x)})
