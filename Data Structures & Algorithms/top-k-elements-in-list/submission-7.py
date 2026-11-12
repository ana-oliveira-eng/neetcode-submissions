class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        s_freq = sorted(freq, key=freq.get)

        return s_freq[-k:]