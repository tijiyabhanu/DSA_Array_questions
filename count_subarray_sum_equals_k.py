class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # BRUTE FORCE
        c=0
        for i in range(0,len(nums)):
            sum=0
            for j in range(i,len(nums)):
                sum+=nums[j]
                if sum==k:
                    c+=1
                    
        return c

        # OPTIMAL APPROACH
        d={0:1}
        sum=0
        c=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            if sum-k in d:

                c+=d[sum-k]
            if sum not in d:
                d[sum]=1
            else:
                d[sum]+=1
        return c
