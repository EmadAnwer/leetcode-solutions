class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
            
            drinked_bottles = 0 # 14
            empty = 0 # 1
            while  numBottles != 0: #0
                drinked_bottles += numBottles # 14
                empty += numBottles # 1
                remain = empty % numExchange #  1
                numBottles = empty // numExchange # 0
                empty = remain # 1


            return drinked_bottles

