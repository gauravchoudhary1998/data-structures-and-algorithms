class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left = 0
        windowProduct = 1
        count = 0

        for right in range(len(nums)):
            windowProduct *= nums[right]

            while windowProduct >= k and left <= right:
                windowProduct //= nums[left]
                left += 1
            
            count += right-left+1

        return count