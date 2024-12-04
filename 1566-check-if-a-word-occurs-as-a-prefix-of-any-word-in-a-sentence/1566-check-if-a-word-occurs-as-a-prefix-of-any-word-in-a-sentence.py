class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        def flag(val,searchWord):
            if len(val) < len(searchWord):
                return False
            for n in range(len(searchWord)):
                if val[n] != searchWord[n]:
                    return False
            return True
        sentence=sentence.split()
        for val in range(len(sentence)):    
            if flag(sentence[val],searchWord):
                return val + 1
        return -1