#!/opt/local/bin/ruby1.9
class String
  def wordValue
    offset = ?A.ord - 1
    return self.chars.inject(0) {|sum, char| sum + char.ord - offset}
  end
end

class Integer
  def triangleNumber?
    i, tn = 0,0
    while (tn < self) do
	i += 1
	tn += i
        return true if self == tn
    end
    false
  end
end

def readWords(fileName)
  words = []
  File.open(fileName, "r") do |infile|
    words = infile.gets.split(",")
  end

  words.map! {|words| words.tr('"', '')}
end


words = readWords("words.txt")
triangleWords = words.select { |word| word.wordValue.triangleNumber?}
puts triangleWords.join(',')
puts triangleWords.length
