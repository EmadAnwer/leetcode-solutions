class Solution(object):
    def threeSum(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[List[int]]
        \\\
        nums.sort()
        t_set = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    t_set.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return [list(t) for t in t_set]