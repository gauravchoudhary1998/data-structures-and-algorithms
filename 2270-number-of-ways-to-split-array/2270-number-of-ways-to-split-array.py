class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixSum = []
        sumn = 0
        count = 0

        for i in range(len(nums)):
            sumn += nums[i]
            prefixSum.append(sumn)

        print(prefixSum)

        for i in range(len(prefixSum)-1):
            if prefixSum[i] >= (prefixSum[-1] - prefixSum[i]):
                count += 1
        
        return count
