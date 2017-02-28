#!/usr/bin/ruby
class CoinCounter
  def initialize(coins)
    @coins = coins.sort
  end
  
  private
    def count_combos(amount, pos)
      return (amount % @coins[pos] == 0 ? 1 : 0) if (pos == 0)
      (0..amount/@coins[pos].floor).inject(0) { |sum, count| sum + count_combos(amount - count * @coins[pos], pos-1) }  
    end
    
  public
    def coin_combinations(amount)
      count_combos(amount, @coins.length-1)
    end
end

cc = CoinCounter.new([1,2,5,10,20,50,100,200])
puts cc.coin_combinations(200)
