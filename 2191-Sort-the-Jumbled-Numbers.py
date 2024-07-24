class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        new_nums = {}


        for i, n in enumerate(nums):
            maped_n = 0
            d = 1
            if n == 0:
                maped_n = mapping[n]
            else:
                while n:
                    maped_n += mapping[n % 10] * d
                    n = n // 10
                    d *=10
            if maped_n in new_nums:
                    new_nums[maped_n].append(nums[i])
            else:
                new_nums[maped_n]= [nums[i]]
                    
        print(new_nums)
        print(sorted(new_nums))

        res = []
        for n in sorted(new_nums):
            res.extend(new_nums[n])
        return res