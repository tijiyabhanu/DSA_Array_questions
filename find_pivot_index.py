class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # OPTIMAL CODE 
        fsum=[]
        lsum=[0]*len(nums)
        ftemp=0
        ltemp=0
        total = sum(nums)
        for i in range(0,len(nums)):
            ftemp+=nums[i]
            fsum.append(ftemp)
        for i in range(len(nums)-1,-1,-1):
            ltemp+=nums[i]
            lsum[i]=ltemp
        for i in range(0,len(nums)):
            if abs(fsum[i]-lsum[i])==0:
                return i
        return -1


        #SPACE OPTIMIZATION CODE
        ftemp=0
        ltemp=0
        total = sum(nums)
        temp=0
        for i in range(0,len(nums)):
            ftemp+=nums[i]
            ltemp=total-temp
            temp=ftemp
            if abs(ftemp-ltemp)==0:
                return i
        return -1
