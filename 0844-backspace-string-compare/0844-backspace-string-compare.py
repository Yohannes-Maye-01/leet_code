class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        arr=[]
        for i in range(len(s)):
            if s[i]!="#":
                arr.append(s[i])
            else:
                if len(arr)!=0:
                     arr.pop()
        arr1=[]        
        for i in  range(len(t)):
            if t[i]!="#":
                arr1.append(t[i])
            else:
                if len(arr1)!=0:
                     arr1.pop()
        if arr==arr1:
            return True
        else:
            return False