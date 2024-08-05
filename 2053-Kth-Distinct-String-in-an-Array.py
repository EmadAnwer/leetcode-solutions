class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        arr_dict = {}

        for s in arr:

            arr_dict[s] = arr_dict.get(s, 0) + 1
        
        for s in arr:
            if arr_dict[s] == 1:
                k -= 1

            if k == 0:
                return s


        return ""
        
                    
        