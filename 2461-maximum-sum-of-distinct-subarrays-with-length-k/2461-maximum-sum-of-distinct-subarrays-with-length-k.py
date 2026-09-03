class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxim = 0
        window_sum = sum(nums[:k])
        freq = {}  # frequency map of current window

        # build initial window freq map
        for i in range(k):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        for i in range(k, len(nums)):
            # check if current window is valid
            if len(freq) == k:
                maxim = max(maxim, window_sum)
            
            # slide window: remove nums[i-k], add nums[i]
            window_sum += nums[i]
            window_sum -= nums[i-k]
            
            # update freq map for incoming element
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            # update freq map for outgoing element
            freq[nums[i-k]] = freq.get(nums[i-k], 0) - 1

            if freq[nums[i-k]] == 0:
                del freq[nums[i-k]]
        
        if len(freq) == k:
            maxim = max(maxim, window_sum)

        return maxim