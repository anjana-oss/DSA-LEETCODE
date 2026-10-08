class Solution(object):
    def isPossibleToSplit(self, nums):
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for c in count:
            if count[c]>2:
                return False
        return True
      

        