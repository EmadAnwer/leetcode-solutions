class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        


        nums.sort()
        
        o, n = nums[0], nums[0]
        for i in range(1, len(nums)):
            o += nums[i]
            if nums[i] <= nums[i - 1]:
                nums[i] =  nums[i - 1]  + 1
            
            n += nums[i]
        return n - o