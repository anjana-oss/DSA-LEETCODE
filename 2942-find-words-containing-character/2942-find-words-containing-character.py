class Solution(object):
    def findWordsContaining(self, words, x):
        result=[]
        for word in range(len(words)):
            for w in words[word]:
                if w==x:
                    result.append(word)
                    break
        return result

