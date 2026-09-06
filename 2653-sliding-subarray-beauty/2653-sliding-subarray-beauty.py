class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        initialWindow = nums[:k]
        freq = {}
        smallest = 0
        
        def getXthSmallest(freq, x):
            count = 0
            for num in range(-50, 0):
                count += freq.get(num, 0)
                if count >= x:
                    return num
            return 0

        for num in initialWindow:
            freq[num] = freq.get(num,0) + 1

        res.append(getXthSmallest(freq, x))

        for i in range(k, len(nums)):
            freq[nums[i-k]] = freq.get(nums[i-k],0) - 1
            freq[nums[i]] = freq.get(nums[i],0) + 1
            smallest = getXthSmallest(freq, x)
            res.append(smallest) 

        return res