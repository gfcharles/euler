#/usr/bin/ruby
def testReduction(a, b) 
  return false if (a % 10 == 0 || b % 10 == 0)
  sa, sb = a.to_s, b.to_s
  if (sa[0] == sb[0]) then
    return sa[1].to_f / sb[1].to_f == a.to_f/b
  elsif (sa[0] == sb[1]) then
    return sa[1].to_f / sb[0].to_f == a.to_f/b
  elsif (sa[1] == sb[0]) then
    return sa[0].to_f / sb[1].to_f == a.to_f/b
  elsif (sa[1] == sb[1]) then
    return sa[0].to_f / sb[0].to_f == a.to_f/b
  end
end

num, den = 1, 1
11.upto(99).each {|a| (a+1).upto(99).each {|b| num,den = num*a, den*b if testReduction(a,b)}}
puts den / num.gcd(den)
