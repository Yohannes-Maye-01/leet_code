class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum=0
        for i in operations:
            if i=="--X":
                sum=sum-1 
            elif i=="X--":
                sum=sum-1
            elif i=="++X":
                sum=sum+1   
            elif i=="X++":
                sum=sum+1
        return  sum      
        
        
        