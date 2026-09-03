class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        avg = sum(arr[:k])
        count = 0

        for i in range(k,len(arr)):
            if avg >= threshold*k:
                count += 1
            avg = avg-arr[i-k]+arr[i]

        if avg >= threshold*k:
            count += 1
        
        return count