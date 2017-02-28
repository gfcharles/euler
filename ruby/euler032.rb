#!/opt/local/bin/ruby1.9
def testTwoThree(n)
  n[0..1].join.to_i * n[2..4].join.to_i == n[5..9].join.to_i
end

def testOneFour(n)
  n[0..0].join.to_i * n[1..4].join.to_i == n[5..9].join.to_i
end
  
products = []
(1..9).to_a.permutation(9) {|p| products << p[5..9].join.to_i if (testOneFour(p) || testTwoThree(p)) }
puts products.uniq.inject {|sum, x| sum + x} 

