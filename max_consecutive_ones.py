class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        c=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                c+=1
                maxi = max(maxi,c)
            else:
                c=0
        return maxi
