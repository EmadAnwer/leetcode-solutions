class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        arr1_dict = {}


        for n in arr1:
            arr1_dict[n] =  arr1_dict.get(n, 0) + 1

        p = 0
        for n in arr2:
            for i in range(arr1_dict[n]):
                arr1[i + p] = n
            p+=arr1_dict[n]
            del arr1_dict[n]

        for n in sorted(arr1_dict.keys()):
            for i in range(arr1_dict[n]):
                arr1[i + p] = n
            p+=arr1_dict[n]
       
        return arr1