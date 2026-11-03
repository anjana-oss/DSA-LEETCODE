class Solution(object):
    def nextPermutation(self, nums):
        i=len(nums)-2
        j=len(nums)-1
        while i>=0:
            if nums[i]<nums[i+1]:
                pivot=nums[i]
                break
            i-=1
        if i==-1:
            left=0
            right=len(nums)-1

            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1

            return
        while j>=0:
            if nums[j]>nums[i]:
                nums[i],nums[j]=nums[j],nums[i]
                break
            j-=1
        
        left=i+1
        right=len(nums)-1

        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        return nums



        

        
        