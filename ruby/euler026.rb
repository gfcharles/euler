#!/usr/bin/ruby
def countPeriod(n)
  n /= 2 while (n % 2 == 0)
  n /= 5 while (n % 5 == 0)
    
  count = 1
  remainder = 10 % n
  while (true) do
    return 0 if (remainder == 0)
    return count if (remainder == 1)
    remainder = (10 * remainder) % n
    count += 1
  end
end

maxPeriod, max = 0, 0
1000.downto(1) do |d|
   period = countPeriod(d)
   maxPeriod, max = period, d if (period > maxPeriod)
   break if (maxPeriod >= d)
end

puts "The max repeat period is #{maxPeriod} for 1/#{max}"

    
