#!/usr/bin/ruby
def nextFib(maxDigits)
  yield 1,1
  yield 2,1
  n = 2
  a, b = 1, 1
  while (b.to_s.length < maxDigits)
    n += 1
    a, b = b, a+b
    yield n, b
  end
end

count = 0
nextFib(1000) {|n,fib| count = n}      
puts count