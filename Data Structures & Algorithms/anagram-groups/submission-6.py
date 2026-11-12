class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = defaultdict(list)

        for w in strs:
            s_strs = str(sorted(w))
            bucket[s_strs].append(w)

        return list(bucket[x] for x in bucket)