class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(s1,s2):
                     return s1.startswith(s2) and s1.endswith(s2)
        count=0
        for i in range(len(words)):
            for j in range(i,len(words)):
                if words[i] is words[j]:
                    continue
                print(f" {words[i]} and {words[j]}")
                if isPrefixAndSuffix(words[j],words[i]):
                    count+=1
        return count


        