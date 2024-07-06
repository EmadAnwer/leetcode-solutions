class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Calculate the cycle length
        cycle_length = 2 * (n - 1)
        
        effective_time = time % cycle_length
        
        if effective_time < n:
            return effective_time + 1
        else:
            return n - (effective_time - n + 1)