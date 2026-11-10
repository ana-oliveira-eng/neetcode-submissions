class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best, l, r = 0, 0 , 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                best = max(best, r - l)
            else:
                seen.remove(s[l])
                l += 1
        return best