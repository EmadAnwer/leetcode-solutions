class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s = set(nums)
        
        for n in nums:
            if n > 0:
                break
            if abs(n) in s:
                return abs(n)

        
        return -1