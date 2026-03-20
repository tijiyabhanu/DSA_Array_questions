class Solution:
    def removeDuplicates(self, arr):
        # code here 
        #BRUTE FORCE
        l1=[]
        for i in arr:
            if i not in l1:
                l1.append(i)
        return l1
        
        # OPTIMAL
        i=0
        c=1
        for j in range(1,len(arr)):
            if arr[i]!=arr[j]:
                arr[i+1]=arr[j]
                i+=1
                c+=1
        return arr[:c]
