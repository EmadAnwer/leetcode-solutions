class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        """
        Given a string s and an integer k. Return the length of the longest substring of s that contains at most k distinct characters.
        """
        dp = [0]  * 26
        res = 0
        
        for i, char in enumerate(s):
            charInd = ord(char) - ord('a')
            leftLimit = max(charInd - k, 0)
            rightLimit = min(charInd + k + 1, 26)
            range_max = max(dp[leftLimit:rightLimit])
            dp[charInd] = max(dp[charInd], range_max + 1)
            res = max(res, dp[charInd])
        return res