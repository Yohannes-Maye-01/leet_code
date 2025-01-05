from collections import defaultdict
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        hash=defaultdict(list)
        for i,num in enumerate(nums):
            hash[num].append(i)
        for k,val in hash.items():
            if len(val)==2:
                ans.append(k)
        print(ans)        
        return ans       


        