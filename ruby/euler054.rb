#!/usr/bin/ruby
module Comparison
  def ==(other)
    (self <=> other) == 0
  end
  
  def !=(other)
    (self <=> other) != 0
  end
  
  def <(other)
    (self <=> other) == -1
  end

  def >(other)
    (self <=> other) == 1
  end
  
  def <=(other)
    self == other || self < other
  end
  
  def >=(other)
    self == other || self > other
  end
end
  
class Suit 
  include Comparison  

  @@suits = {"C" => [0,"clubs"], "D" => [1,"diamonds"], "H" => [2,"hearts"], "S" => [3,"spades"]}
  attr_reader :suitCode

  def initialize(suitCode)
    @suitCode = suitCode
  end
  
  def value
    @@suits[suitCode][0]
  end
  
  def <=>(other)
    self.value <=> other.value
  end

  def to_s
    @@suits[suitCode][1]
  end
end

class Rank
  include Comparison
  
  @@ranks = {  "2" => [2,"Two"], "3" => [3,"Three"], "4" => [4, "Four"], "5" => [5, "Five"], 
               "6" => [6, "Six"], "7" => [7, "Seven"], "8" => [8, "Eight"], "9" => [9, "Nine"],
               "T" => [10, "Ten"], "J" => [11, "Jack"], "Q" => [12, "Queen"], "K" => [13, "King"], "A" => [14, "Ace"]
            }
   
  attr_reader :rankCode
    
  def initialize(rankCode)
    @rankCode = rankCode
  end

  def value
    @@ranks[rankCode][0]
  end
      
  def <=>(other)
    self.value <=> other.value
  end
  
  def to_s
    @@ranks[rankCode][1]
  end
end

class Card
  include Comparison
  
  attr_reader :rank
  attr_reader :suit
  
  def initialize(cardCode)
    @rank = Rank.new(cardCode[0])
    @suit = Suit.new(cardCode[1])
  end
  
  def <=>(other)
    self.rank <=> other.rank
  end
  
  def to_s
    "#{rank}" # of #{suit}"
  end
end

class Hand
  include Comparison
  attr_reader :cards, :handType, :handCards, :kickers

  @@values = ["nothing", "pair", "two pairs", "three-of-a-kind", "straight", "flush", 
              "full house", "four-of-a-kind", "straight flush"]
    
  def initialize(cardCodes)
    @cards = cardCodes.each.inject([]) {|cards, cardCode| cards << Card.new(cardCode)}.sort
    evaluateHand()
  end
  
  def evaluateHand()
    valueString = @cards.map {|card| card.rank.value.to_s(16)}.join
    @handCards = valueString 
    @kickers = []
    
    if matchPattern(valueString, /(.)\1\1\1/)
       @handType = "four-of-a-kind" 
    elsif matchPattern(valueString, /(.)\1(.)\2\2/)
      @handType = "full house"
    elsif matchPattern(valueString, /(.)\1\1(.)\2/)
      @handType = "full house"
      specialFullHouseProcessing
    elsif matchPattern(valueString, /(.)\1\1/)
      @handType = "three-of-a-kind"
    elsif matchPattern(valueString, /(.)\1(.)\2/)
      @handType = "two pairs"
    elsif matchPattern(valueString, /(.)\1.(.)\2/)
      @handType = "two pairs"
      specialTwoPairsProcessing
    elsif matchPattern(valueString, /(.)\1/)
      @handType = "pair"
    end
    
    if @handType == nil then
      suitString = @cards.map {|card| card.suit.value.to_s()}.join
      straight = straight?(valueString)
      flush = flush?(suitString)

      if straight && flush
        @handType = "straight flush"
      elsif straight
        @handType = "straight" 
      elsif flush
        @handType = "flush"
      else
        @handType = "nothing"
      end
    end
  end
  
  def matchPattern(valueString, pattern)
    match = valueString.match(pattern)
    return false if match == nil
    
    @handCards = match[0]
    @kickers = valueString.sub(match[0], "")
  end

  def specialFullHouseProcessing
    @handCards = @handCards[3..4] + @handCards[0..2]
  end
  
  def specialTwoPairsProcessing
    @kickers = @handCards[2]
    @handCards = @handCards[0..1] + @handCards[3..4]
  end

  def straight?(valueString)
    return valueString[4].to_i(16) - valueString[0].to_i(16) == 4
  end
  
  def flush?(suitString)
    return suitString.match(/(.)\1\1\1\1/)
  end
  
  def <=>(other)
    return @@values.index(self.handType) <=> @@values.index(other.handType) if (self.handType != other.handType)
    
    (1..self.handCards.length).each {|i| value = self.handCards[-i].to_i(16) <=> other.handCards[-i].to_i(16); return value if value != 0}
    (1..self.kickers.length).each {|i| value = self.kickers[-i].to_i(16) <=> other.kickers[-i].to_i(16); return value if value != 0}
    0
  end
  
  def to_s
    self.cards.join(", ")
  end
end

sum = 0
File.open("poker.txt", "r") do |infile|
  while (line = infile.gets)
    cards = line.split(" ")
    hand1, hand2 = Hand.new(cards[0..4]), Hand.new(cards[5..9])
    puts [hand1,  ' vs ', hand2].join(' ')
    puts [hand1.handType, hand2.handType, hand1 <=> hand2].join(', ')
    sum += 1 if hand1 > hand2
  end
end

puts sum


