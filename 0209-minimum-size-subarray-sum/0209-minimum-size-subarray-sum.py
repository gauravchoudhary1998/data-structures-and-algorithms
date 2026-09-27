class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        window_sum = 0
        result = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]        # expand window

            while window_sum >= target:
                result = min(result, right-left+1)   # update result
                window_sum -= nums[left]          # shrink window
                left += 1
        
        if result == float('inf'):
            return 0

        return result