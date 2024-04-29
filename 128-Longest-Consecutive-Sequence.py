class Solution(object):
    def longestConsecutive(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        largest = 0
        mydit = {}
        
        for n in nums:
            if n not in mydit:
                left = mydit.get(n-1, 0)
                right = mydit.get(n+1, 0)
                length = left + right + 1
                mydit[n] = length
                mydit[n-left] = length
                mydit[n+right] = length
                largest = max(largest, length)
        return largest