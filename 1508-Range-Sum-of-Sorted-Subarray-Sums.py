class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7

        new_arr = []

        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                new_arr.append(current_sum)

        return sum(sorted(new_arr)[left - 1 : right]) % MOD