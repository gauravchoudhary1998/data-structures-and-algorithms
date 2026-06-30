class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sumn = 0
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        print(nums)

        for i in range(len(nums)):
            if i <= 0:
                leftSum = 0
            else:
                leftSum = nums[i-1]

            if i >= len(nums)-1:
                rightSum = 0
            else:
                rightSum = nums[-1]-nums[i]

            if leftSum == rightSum:
                return i
        return -1