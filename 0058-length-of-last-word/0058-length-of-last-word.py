class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        for j in range(len(s)-1,-1,-1):
            if count==0 and s[j]==" ":
                continue
            if s[j]==" ":
                return count
            else:
                count+=1
        return count