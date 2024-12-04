class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split()
        for i,val in enumerate(sentence):
            if val.startswith(searchWord):
                return i + 1
        
        return -1