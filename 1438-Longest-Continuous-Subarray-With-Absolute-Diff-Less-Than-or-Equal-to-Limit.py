
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()  # Deque to store the maximum values
        min_deque = deque()  # Deque to store the minimum values
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            # Maintain the max deque
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain the min deque
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Check if the current window is valid
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # Remove elements that are out of the current window
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Update the maximum length of the valid subarray
            max_len = max(max_len, right - left + 1)
        
        return max_len








# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:

#         max_len = 0
#         for i in range(len(nums)):
#             for j in range(i , len(nums)):
#                 max_n = nums[i]
#                 min_n = nums[i]
#                 for x in range(i, j + 1):
#                     max_n = max(max_n, nums[x])
#                     min_n = min(min_n, nums[x])
                
#                 if max_n - min_n <= limit:
#                     max_len = max(j + 1 - i, max_len)
                

#         return max_len

