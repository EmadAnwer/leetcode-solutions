class Solution(object):
    def maxArea(self, height):
        \\\
        :type height: List[int]
        :rtype: int
        \\\
        l, r = 0, len(height) - 1
        max_amount = 0
        while l < r:
            area =  (r - l) * min(height[l], height[r])
            max_amount = max(max_amount, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_amount