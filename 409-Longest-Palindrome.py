class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_list = [0] * 52

        for l in s:
            if 'a' <= l <= 'z': 
                letter_list[ord(l) - ord('a')] += 1
            elif 'A' <= l <= 'Z':  
                letter_list[ord(l) - ord('A') + 26] += 1

        res = 0
        odd_found = False

        for count in letter_list:
            if count % 2 == 0:
                res += count
            else:
                res += count - 1 
                odd_found = True  

        if odd_found:
            res += 1 

        return res