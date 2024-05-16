class Solution(object):
    def isValid(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\

        stack = []
        parentheses = {
            \(\:\)\,
             \[\:\]\,
             \{\:\}\
        }

        for p in s:
            if p in parentheses:
                stack.append(p)
            elif len(stack) == 0 or parentheses[stack.pop()] != p:
                return False
        return len(stack) == 0