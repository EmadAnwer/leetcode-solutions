class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Initialize counters
        b_count = 0
        deletions = 0

        for char in s:
            if char == 'b':
                b_count += 1
            elif char == 'a':
                # If we encounter 'a', we have two choices:
                # 1. Delete this 'a' and increment deletions.
                # 2. Delete one of the previous 'b's.
                # We'll choose the minimum deletions required.
                deletions = min(deletions + 1, b_count)
        
        return deletions