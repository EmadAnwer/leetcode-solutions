class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_count = {0: 1}  # Initialize with 0:1 to handle the case when the prefix sum itself is divisible by k

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            # Normalize the remainder to be within the range [0, k-1]
            if remainder < 0:
                remainder += k

            # If this remainder has been seen before, it means there are subarrays ending here that sum to a multiple of k
            if remainder in remainder_count:
                count += remainder_count[remainder]

            # Increment the count of this remainder in the hash map
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return count