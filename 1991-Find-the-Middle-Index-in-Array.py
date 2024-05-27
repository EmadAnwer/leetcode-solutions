class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        left_sum = 0
        right_sum = 0
        for n in nums:
            right_sum += n
            
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1
        