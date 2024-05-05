class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        
        seen = set()
        max_k = float('-inf')

        for n in nums:
            if -n in seen:
                max_k = max(max_k, abs(n))
            seen.add(n)

        return max_k if max_k != float('-inf') else -1