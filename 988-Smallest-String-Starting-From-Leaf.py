# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        m  = None

        def rec(root = root, mystr=""):
            nonlocal m
            if root == None:
                return
            if not root.left and not root.right:
                mystr+= chr(97 + root.val)
                if m == None:
                    m = mystr[::-1]
                    
                if m == None:
                    m = mystr
                m  = min(m , mystr[::-1] )
                return 
            
          
            mystr+= chr(97 + root.val)
            rec(root.left, mystr)
            rec(root.right, mystr)
            

        rec()

        return m

        