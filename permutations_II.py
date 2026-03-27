from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        for i in  permutations(nums):
            res.append(i)
        return list(set(res))
