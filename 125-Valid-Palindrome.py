class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = [c.lower() for c in s if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9']
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True