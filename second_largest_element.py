class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        # BRUTE FORCE
        arr.sort()
        m=arr[-1]
        sl=-1
        for i in range(len(arr)-1,-1,-1):
            if arr[i]<m and arr[i]!=m:
                sl=arr[i]
                break
        return sl
        
        # BETTER APPROACH
        fm=arr[0]
        sm=-1
        for i in arr:
            if i>fm:
                fm=i
        for i in arr:
            if i>sm and i<fm:
                sm=i
        return sm
        
        # OPTIMAL APPROACH
        fm=arr[0]
        sm=-1
        for i in arr:
            if i>fm:
                sm=fm
                fm=i
            elif i<fm and i>sm:
                sm=i
        return sm
