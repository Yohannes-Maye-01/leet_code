class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split()
        searchWord=list(searchWord)
        j=len(searchWord)
        for i,val in enumerate(sentence):
            val=list(val)
            if val[0:j]==searchWord:
                        index=i+1
                        return index
        
        return -1