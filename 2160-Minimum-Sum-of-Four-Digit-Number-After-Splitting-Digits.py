class Solution:
    def minimumSum(self, num: int) -> int:
        
        num_list = [0]* 4 

        for i in range(4):
            num_list[i] = num % 10
            num //= 10
        
        num_list.sort()
        n1 = num_list[0] * 10 + num_list[3]
        n2 = num_list[1] * 10 + num_list[2]



        return n1 + n2