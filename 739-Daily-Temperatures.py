class Solution(object):
    def dailyTemperatures(self, temperatures):
        \\\
        :type temperatures: List[int]
        :rtype: List[int]
        \\\
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                temperatures[idx] = i - idx
            stack.append(i)
        while stack:
            idx = stack.pop()
            temperatures[idx] = 0
        return temperatures