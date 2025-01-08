# class Solution:
#     def countPrefixSuffixPairs(self, words: List[str]) -> int:
#         def isPrefixAndSuffix(s1,s2):
#                     return s1.startswith(s2) and s1.endswith(s2)
#         count=0
#         for i in range(len(words)):
#             for j in range(i,len(words)):
#                 if words[i] is words[j]:
#                     continue
#                 print(f" {words[i]} and {words[j]}")
#                 if isPrefixAndSuffix(words[j],words[i]):
#                     count+=1
#         return count
        



# class Solution:
#     def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
#         n1, n2 = len(str1), len(str2)
#         if n1 > n2:
#             return False
#         return str2[:n1] == str1 and str2[-n1:] == str1

#     def countPrefixSuffixPairs(self, words: List[str]) -> int:
#         n = len(words)
#         count = 0
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if self.isPrefixAndSuffix(words[i], words[j]):
#                     count += 1
#         return count




# class Solution:
#     def countPrefixSuffixPairs(self, words: List[str], ans = 0) -> int:

#         for pre_suf, word in combinations(words,2):
#             ans+= word.startswith(pre_suf) and word.endswith(pre_suf)

#         return  ans 








class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            s1 = words[i]
            for j in range(i + 1, n):
                s2 = words[j]
                if len(s2) < len(s1):
                    continue
                pre = s2[:len(s1)]
                suf = s2[-len(s1):]
                if pre == s1 and suf == s1:
                    ans += 1
        return ans        