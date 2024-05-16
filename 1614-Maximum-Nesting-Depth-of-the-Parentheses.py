class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        depth = 0
        level = 0
        for c in s:
            if  c =="(":
                level+=1
            elif c == ")":
                level-=1
            
            depth = max(depth, level)
        
        return depth