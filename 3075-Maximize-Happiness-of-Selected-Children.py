class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        m = happiness[0]
        for i in range(1, k):
            c = happiness[i] - i
            m += max(0, c)
        
        return m