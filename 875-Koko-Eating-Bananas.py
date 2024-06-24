# import math
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
#         k = 0
#         while True:
#             k += 1
#             o = 0
#             for p in piles:
#                 o += math.ceil(p / k)
#                 if o > h:
#                     break

#             if o - h == 0:
#                 break
#         return k



import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours  <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
            

        return res