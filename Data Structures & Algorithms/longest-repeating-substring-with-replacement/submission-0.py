class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, best = 0, 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l+=1

            best = max(best, r - l + 1) 
        return best
