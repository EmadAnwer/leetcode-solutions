class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_map = {}

        for n in nums:
            if n in nums_map:
                nums_map[n] += 1
            else:
                nums_map[n] = 1
        
        busket = [None] * len(nums)


        for key, value in nums_map.items():

            if busket[value - 1] == None:
                busket[value - 1] = [key]
            else:
                busket[value - 1].append(key)
        
        res = []

        while k:
            f = busket.pop()
            if f:
                res.extend(f)
                k -= len(f)

            
        return res