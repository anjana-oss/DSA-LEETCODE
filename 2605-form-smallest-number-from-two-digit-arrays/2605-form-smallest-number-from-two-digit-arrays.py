class Solution(object):
    def minNumber(self, nums1, nums2):
        common=[]
        for x in nums1:
            if x in nums2:
                common.append(x)
        if common:
            ans=min(common)
            return ans


        min1=min(nums1)
        min2=min(nums2)
        val1=min1*10+min2
        val2=min2*10+min1

        if val1>val2:
            return val2
        else:
            return val1