class Solution(object):
    def evalRPN(self, tokens):
        \\\
        :type tokens: List[str]
        :rtype: int
        \\\

        stack = []
        
        for t in tokens:
            if t not in '+-/*':
                stack.append(int(t))
                continue
            n1, n2 = stack.pop(), stack.pop()
            if t == '+':
                stack.append(n2 +  n1)
            elif t == '-':
                stack.append(n2 -  n1)
            elif t == '*':
                stack.append(n2 *  n1)
            elif t == '/':
                stack.append(int(float(n2) / n1))

            
        return stack.pop()