class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        maxLen = 0
        zeroCount = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1        # expand, track zeros

            while zeroCount > k:      # window invalid, shrink
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            
            maxLen = max(maxLen, right-left+1) 
        return maxLen