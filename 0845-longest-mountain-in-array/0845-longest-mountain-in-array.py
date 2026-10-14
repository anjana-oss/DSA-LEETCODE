class Solution(object):
    def longestMountain(self, arr):
        n=len(arr)
        max_len=0
        curr=0
        for i in range(1,len(arr)-1):
            if  arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                left=i
                right=i
                curr+=1
                while left>0 and  arr[left-1]<arr[left]:
                    left-=1
                else:
                    while right<n-1 and  arr[right]>arr[right+1]:
                        right+=1
                curr=right-left+1 


            if curr>max_len:
                 max_len=curr
        return max_len

        