class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for i in range(len(words)):
            res="".join(words[0:i+1])
            print(res)

            if  res==s:
                    return True
        return False

        