class Solution(object):
    def longestConsecutive(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        largest = 0
        nums_set = set(nums)

        for n in nums_set:
            if n - 1 not in nums_set:
                length = 0
                while n + length in nums_set:
                    length += 1
                largest = max(largest, length)  
        return largest