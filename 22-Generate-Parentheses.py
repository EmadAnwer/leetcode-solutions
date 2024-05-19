class Solution(object):
    def generateParenthesis(self, n):
        \\\
        :type n: int
        :rtype: List[str]
        \\\
        stack = []
        res = []


        def bt(o, c):
            if o == c == n:
                res.append(\\.join(stack))
                return
            

            if o < n:
                stack.append(\(\)
                bt(o+1, c)
                stack.pop()
            
            if c < o:
                stack.append(\)\)
                bt(o, c + 1)
                stack.pop()
        
        bt(0,0)

        return res