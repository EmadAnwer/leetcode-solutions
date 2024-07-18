class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        max_c = 0
        for n in nums:
            if n - 1 not in nums:
                current = n
                count = 1
                while current + 1 in nums:
                    count += 1
                    current+= 1

                
                max_c = max(count, max_c)
        
        return max_c