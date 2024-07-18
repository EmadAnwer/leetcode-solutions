class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = None

        has_zero = 0

        for n in nums:

            if n == 0:
                has_zero += 1
            else:
                if total:
                    total *= n
                else:
                    total = n
        
        if has_zero == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = total
                else:
                    nums[i] = 0
        elif has_zero > 1:
            for i in range(len(nums)):
                nums[i] = 0
        else:
            for i in range(len(nums)):
                nums[i] = total // nums[i]
        

        return nums

