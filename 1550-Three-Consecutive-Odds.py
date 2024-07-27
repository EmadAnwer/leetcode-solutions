class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        

        odds_c = 0

        for n in arr:
            if n % 2:
                odds_c += 1
            else:
                odds_c = 0
            
            if odds_c == 3:
                return True
        
        return False