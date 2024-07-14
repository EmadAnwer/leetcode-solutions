class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        res = ""
        
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        for i in range(len(s)):
            # Check for odd length palindromes
            odd_palindrome = expandAroundCenter(i, i)
            if len(odd_palindrome) > len(res):
                res = odd_palindrome
            
            # Check for even length palindromes
            even_palindrome = expandAroundCenter(i, i + 1)
            if len(even_palindrome) > len(res):
                res = even_palindrome
        
        return res

        





        
