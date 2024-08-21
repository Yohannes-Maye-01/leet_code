class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i in '({[': 
                stk.append(i)
            elif i in ')}]':  
                if not stk: 
                    return False
                x = stk.pop()
                if (x == '(' and i == ')') or (x == '{' and i == '}') or (x == '[' and i == ']'):
                    continue
                else:
                    return False
        return len(stk) == 0  
