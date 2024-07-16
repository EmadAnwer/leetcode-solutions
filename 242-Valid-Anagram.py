class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):
            return False

        
        chars = [0] * 26

        for c1, c2 in zip(s, t):
            chars[ord(c1)- 97] += 1
            chars[ord(c2)- 97] -= 1

        for n in chars:
            if n != 0:
                return False
        return True