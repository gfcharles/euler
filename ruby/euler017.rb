#!/usr/bin/ruby
def hasAnd?(british, n)
  return false unless british
  n > 100 && n % 100 != 0
end

def getNormalNumberString(n)
  getNumberString(n, false)
end

def getBritishNumberString(n)
  getNumberString(n, true)
end

def getNumberString(n, british)
  powers = ['', 'thousand', 'million', 'billion', 'trillion']

  num = n.to_s
  numberString = ''
  length = 0
  count = 0
  while (num.length > 3) 
    l, s = getThreeDigitString(num.slice!(-3..-1).to_i, british)
    if (l > 0) 
      length += (l + powers[count].length) 
      numberString = append(append(s, powers[count]), numberString)
    end
    count += 1
  end
  if (num.length > 0) 
    l, s =  getThreeDigitString(num.to_i, british)
    if (l > 0) 
      length += (l + powers[count].length) 
      numberString = append(append(s, powers[count]), numberString)
    end
  end
  return length, numberString
end
  
  
def getThreeDigitString(n, british)
  return 0, '' if (n == 0)
  
  ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 
     'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
     
  tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eigthy', 'ninety']

  hundred = 'hundred'
  andSymbol = 'and'

  d1 = n / 100
  d2 = n % 100 / 10
  d3 = (d2 < 2) ? n % 20 : n % 10
 
  hasAnd = hasAnd?(british, n)
  
  length = (ones[d1].length + (d1 == 0 ? 0 : hundred.length) + tens[d2].length + ones[d3].length + (hasAnd ? andSymbol.length : 0))

  s1 = ones[d1]
  s2 = tens[d2]
  s3 = ones[d3]
  s_and = (hasAnd ? andSymbol : '')
  
  numberString = ''
  numberString = append(numberString, s1)
  numberString = append(numberString, hundred) if d1 != 0
  numberString = append(numberString, s_and)
  numberString = append(numberString, s2)
  numberString = append(numberString, s3)
  
  return length, numberString
end

def append(str, s)
  if str.length == 0
    s
  elsif s.length == 0
    str
  else
    str + ' ' + s
  end
end
 
length = 0
1.upto(1000) {|n|  puts getBritishNumberString(n)[1] }
1.upto(1000) {|n|  length += getBritishNumberString(n)[0] }
puts length

puts getNormalNumberString(10000000002)
  
