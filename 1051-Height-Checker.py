class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        sorted_heights = sorted(heights)

        not_expected = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                not_expected+= 1
        

        return not_expected