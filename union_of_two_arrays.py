class Solution:    
    def findUnion(self, a, b):
        # code here
        a.sort()
        b.sort()
        u=[]
        # u.append(a[0])
        j=0
        i=0
        while(i<len(a) and j<len(b)):
            if a[i]<b[j]:
                if not u or a[i]!=u[-1]:
                    u.append(a[i])
                i+=1
            elif a[i]>b[j]:
                if not u or b[j]!=u[-1]:
                    u.append(b[j])
                j+=1
            else:
                if not u or a[i]!=u[-1]:
                    u.append(a[i])
                i+=1
                j+=1
        while(j<len(b)):
            if not u or b[j]!=u[-1]:
                u.append(b[j])
            j+=1
        while(i<len(a)):
            if not u or a[i]!=u[-1]:
                u.append(a[i])
            i+=1
        return u
