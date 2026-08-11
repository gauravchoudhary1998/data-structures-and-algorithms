class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            max_prev = max_so_far
            # min_prev = min_so_far

            max_so_far = max(nums[i], max_prev * nums[i], min_so_far * nums[i])
            min_so_far = min(nums[i], max_prev * nums[i], min_so_far * nums[i])
            ans = max(ans,max_so_far)
        return ans

        
        
