class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      # BRUTE FORCE
        vis = [0]*len(nums2)
        res=[]
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if nums1[i]==nums2[j] and vis[j]==0:
                    if not res or res[-1]!=nums2[j]:
                        res.append(nums2[j])
                    vis[j]=1
        return res
            
      # OPTIMAL APPROACH
        i=0
          j=0
          res=[]
          nums1.sort()
          nums2.sort()
          while(i<len(nums1) and j<len(nums2)):
              if nums1[i]<nums2[j]:
                  i+=1
              elif nums1[i]>nums2[j]:
                  j+=1
              elif nums1[i]==nums2[j]:
                  if not res or res[-1]!=nums1[i]:
                      res.append(nums1[i])
                  i+=1
                  j+=1
          return res
