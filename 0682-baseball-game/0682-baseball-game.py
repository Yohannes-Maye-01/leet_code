class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        
        for i in operations:
            if i.lstrip("-").isdigit():  
                stk.append(int(i))  
            elif i == "C":
                stk.pop()  
            elif i == "D":
                stk.append(stk[-1] * 2)
            elif i == "+":
                stk.append(stk[-1] + stk[-2]) 
        
        return sum(stk) 

                
        