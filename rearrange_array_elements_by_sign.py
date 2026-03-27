class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # BRUTE FORCE
        pos=[]
        neg=[]
        res=[]
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        for i in range(0,len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res
        # OPTIMAL APPROACH 
        i,j=0,1
        res=[0]*len(nums)
        for k in range(0,len(nums)):
            if nums[k]>0:
                # temp=nums[i]
                res[i]=nums[k]
                i+=2
            else:
                res[j]=nums[k]
                j+=2
        return res
