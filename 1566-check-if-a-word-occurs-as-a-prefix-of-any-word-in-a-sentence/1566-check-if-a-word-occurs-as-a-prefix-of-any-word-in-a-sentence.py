class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split()
        j=len(searchWord)
        for i,val in enumerate(sentence):
            flag = True
            for n in range(j):
                if j > len(val):
                    flag = False
                    break
                if val[n] != searchWord[n]:
                    flag = False
            if flag:
                return i + 1
        
        return -1