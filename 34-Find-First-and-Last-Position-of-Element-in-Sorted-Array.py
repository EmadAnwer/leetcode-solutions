class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                if m == 0 or nums[m - 1] != target:
                    res[0] = m
                    break
                else:
                    r = m - 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        if res[0] == -1:
            return res

        l, r = res[0], len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                if m == len(nums) - 1 or nums[m + 1] != target:
                    res[1] = m
                    break
                else:
                    l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
                
        return res