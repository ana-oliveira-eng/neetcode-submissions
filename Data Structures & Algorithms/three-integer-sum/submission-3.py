class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, j, k = 0, 1, len(nums) - 1
        res = []
        nums.sort()
        while i < len(nums):
            target = -nums[i]
            while j < k:
                s = nums[j] + nums[k]
                if s == target:
                    op = [nums[i], nums[j], nums[k]]
                    if op not in res:
                        res.append(op)
                    j+=1
                elif s > target:
                    k-= 1
                elif s < target:
                    j+=1
            i+=1
            j=i+1
            k=len(nums)-1
        return res