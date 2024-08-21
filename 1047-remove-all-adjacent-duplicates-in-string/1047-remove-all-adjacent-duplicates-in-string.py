class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk=[]
        for i in s:
            if len(stk)!=0:
                if stk[len(stk)-1]==i:
                    stk.pop()
                    continue
              
            stk.append(i)
        return ''.join(stk)            
        