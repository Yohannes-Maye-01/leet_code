# from collections import defaultdict
# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
#         s=list(s)
#         c=0
#         windowcollict=defaultdict(list)
#         window=[]
#         for i in range(len(s)):
#             l=i+1
            
#             while l<len(s):
#                 r=l+1
#                 while r<len(s):
#                     window=[s[i],s[l],s[r]]
#                     print(window) 
#                     if  window== window[::-1]:
#                        wind=tuple(window)  
#                        windowcollict[wind]=window
#                     print(windowcollict) 
#                     r=r+1
#                 l=l+1
#         return len(windowcollict)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in set(s):  # Iterate over unique characters
            i, j = s.find(c), s.rfind(c)  # First and last occurrence
            if j > i + 1:  # Ensure there's at least one element between
                res += len(set(s[i+1:j]))  # Count unique middle elements
        return res