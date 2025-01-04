class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        a = 1
        if k > 0:
            a*=1
            l = code[:k]
            s = code+l
        else:
            a*=-1
            l = code[k:]
            k*=-1
            s = l+code
        print(s)
        res = []
        cul = []
        for i in range(k):
            cul.append(s[i])
        res.append(sum(cul))
        if not cul:
            return [0]*len(code)
        for i in range(k,len(s)):
            cul.pop(0)
            cul.append(s[i])
            if len(cul)==k:
                res.append(sum(cul))
        if a==1:
            return res[1:]
        return res[:-1]

            


# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         n=len(code)
#         ans=[0]*n
#         if k==0: return ans
#         if k>0:
#             ans[0]=wsum=sum(code[1:k+1])
#             for l in range(1, n):
#                 r=(l+k)%n
#                 wsum+=-code[l]+code[r]
#                 ans[l]=wsum
#             return ans
#         # Python has minus index
#         ans[0]=wsum=sum(code[-1:k-1:-1])
#         for l in range(1, n):
#             r=(l-k)%n
#             wsum+=-code[-l]+code[-r]
#             ans[-l]=wsum
#         return ans
        
        