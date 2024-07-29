class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0

        for m in range(1, len(rating) - 1):
            left_less, left_more = 0, 0
            right_less, right_more = 0, 0

            for i in range(m):
                if rating[i] < rating[m]:
                    left_less += 1
                else:
                    left_more += 1

            for j in range(m + 1, len(rating)):
                if rating[j] < rating[m]:
                    right_less += 1
                else:
                    right_more += 1

            res += left_less * right_more + left_more * right_less

        return res
