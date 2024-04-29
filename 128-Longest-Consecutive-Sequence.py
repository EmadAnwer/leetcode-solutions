class Solution(object):
    def longestConsecutive(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        largest = 0
        mydict = {}
        
        for n in nums:
            if n not in mydict:
                left = mydict.get(n-1, 0)
                right = mydict.get(n+1, 0)
                length = left + right + 1
                mydict[n] = length
                mydict[n-left] = length
                mydict[n+right] = length
                largest = max(largest, length)
        return largest