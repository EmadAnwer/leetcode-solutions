class Solution:
    def checkRecord(self, s: str) -> bool:
        
        a = 0
        l = 0
        for d in s:
            if d == "L":
                l += 1
                if l == 3:
                    return False
            else:
                l = 0
            if d == "A":
                a+=1
                if a == 2:
                    return False
            
        return True


                