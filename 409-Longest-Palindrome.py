class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}

        for l in s:
            dic[l] = dic.get(l, 0) + 1

        res = 0
        odd_found = False

        for count in dic.values():
            if count % 2 == 0:
                res += count
            else:
                res += count - 1
                odd_found = True  

        if odd_found:
            res += 1

        return res