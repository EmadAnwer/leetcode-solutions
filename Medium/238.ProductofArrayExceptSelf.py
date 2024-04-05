class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 1
        has_zero = False
        zeros = 0

        for n in nums:
            if n != 0:
                total *= n
            else:
                has_zero = True
                zeros += 1

        if zeros == len(nums):
            return nums
        for i in range(len(nums)):
            if has_zero:
                if nums[i] == 0 and zeros == 1:
                    nums[i] = total
                else:
                    nums[i] = 0
            else:
                # without division

                nums[i] = total // nums[i]
        return nums


s = Solution()
nums = [1, 2, 3, 4]
print(s.productExceptSelf(nums))
