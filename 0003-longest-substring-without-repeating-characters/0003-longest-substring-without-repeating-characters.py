class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        smap = {}
        maxWindow = 0

        for i in range(len(s)):
            if s[i] in smap and smap[s[i]] >= left:
                left = smap[s[i]]+1

            smap[s[i]] = i
            maxWindow = max(maxWindow, i - left + 1)

        return maxWindow 