class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_hash = {}

        for i, n in enumerate(nums):
            if target - n in idx_hash:
                return [i, idx_hash[target - n]]
            idx_hash[n]= i
            