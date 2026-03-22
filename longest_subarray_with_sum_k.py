class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        #BRUTE FORCE IS USING TWO FOR LOOPS 
        #THIS IS THE OPTIMAL ONE USING PREFIX SUM AND HASHING
        d={0:-1}
        sum=0
        maxlen=0
        for i in range(0,len(arr)):
            sum+=arr[i]
            if sum not in d:
                d[sum]=i
            if sum-k in d:
                maxlen = max(i-d[sum-k],maxlen)
        
        return maxlen
