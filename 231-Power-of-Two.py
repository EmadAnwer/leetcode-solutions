class Solution(object):
    def isPowerOfTwo(self, n):
        \\\
        :type n: int
        :rtype: bool
        \\\
        if n == 0:
            return False

        while n != 0:
            
            if n % 2 != 0 and n != 1:
                return False
            n /= 2
        

        return True
        