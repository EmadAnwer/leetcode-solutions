class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splited_path = path.split(\/\)

        for d in splited_path:
            if d == \..\:
                if len(stack) != 0:
                    stack.pop()
            elif d != \\ and d != \.\:
                stack.append(d)

        return f\/{'/'.join(stack)}\