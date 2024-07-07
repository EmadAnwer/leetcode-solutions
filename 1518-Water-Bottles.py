class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drinked_bottles = numBottles
        
        while numBottles >= numExchange:
            new_bottles = numBottles // numExchange
            total_drinked_bottles += new_bottles
            numBottles = new_bottles + (numBottles % numExchange)
        
        return total_drinked_bottles