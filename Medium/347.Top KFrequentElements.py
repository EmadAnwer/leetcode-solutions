class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequents = {}

        for n in nums:

            if not frequents.get(n):
                frequents[n] = 1
            else:
                frequents[n] += 1
        sorted_items = sorted(frequents.items(), key=lambda a: a[1], reverse=True)

        return [sorted_items[i][0] for i in range(k)]


s = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(s.topKFrequent(nums, k))
