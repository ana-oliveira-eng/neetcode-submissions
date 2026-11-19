class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        freq_1 = {}

        for char in s1:
            freq_1[char] = freq_1.get(char, 0) + 1

        freq_2 = {}

        while r < len(s2):
            if s2[r] in s1:
                freq_2[s2[r]] = freq_2.get(s2[r], 0) + 1

                while freq_2[s2[r]] > freq_1[s2[r]]:
                    freq_2[s2[l]] -= 1
                    if freq_2[s2[l]] == 0:
                        del freq_2[s2[l]]
                    l += 1

                if freq_1 == freq_2:
                    return True

            else:
                l = r + 1
                freq_2 = {}

            r += 1

        return False