class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = defaultdict(int)

        for n in nums:
            s[n]+=1

        return max(s, key=s.get)