#!/usr/bin/ruby
def collatzCount(n) 
  count = 1
  while n != 1 
    if (n%2 == 0) 
      n = n / 2
    else
      n = 3 * n + 1
    end
    count += 1
  end
  
  return count
end

maxTerms = 0
maxN = 0
n = 500_001
beginning = Time.now
while n < 1_000_000 
  collatzCount = collatzCount(n)
  if (collatzCount > maxTerms) 
    maxTerms, maxN = collatzCount, n
  end
  n += 2
end

puts "Time elapsed #{Time.now - beginning} seconds"
puts maxTerms, maxN
    
