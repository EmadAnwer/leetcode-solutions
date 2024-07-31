from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        cache = {}

        def dp(i):
            if i == len(books):
                return 0
            if i in cache:
                return cache[i]
            cur_width = shelfWidth
            max_height = 0

            cache[i] = float('inf')

            for j in range(i, len(books)):
                if books[j][0] > cur_width:
                    break
                cur_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                cache[i] = min(cache[i], max_height + dp(j + 1))
            return cache[i] 
        

        return dp(0)