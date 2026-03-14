class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for index,value in enumerate(nums):
            rem = target-value
            if rem in d:
                return [d[rem],index]
            d[value]=index
