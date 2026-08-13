class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)   # total sum upfront
        left  = 0           # running left sum
        count = 0

        for i in range(len(nums)-1):
            left += nums[i]
            if left >= total - left:
                count += 1
        return count
