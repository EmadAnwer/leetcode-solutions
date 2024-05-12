class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        index_map = {} 
        
        for i, char in enumerate(s):
            index_map[char] = i
        
        permutation_diff = 0
        
        for i, char in enumerate(t):
            permutation_diff += abs(i - index_map[char])
        
        return permutation_diff