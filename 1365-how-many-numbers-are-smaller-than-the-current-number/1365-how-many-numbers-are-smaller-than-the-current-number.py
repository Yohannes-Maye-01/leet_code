class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0] * 101
        for i in nums:
            cnt[i] += 1
        for i in range(1, 101):
            cnt[i] += cnt[i - 1]
        return [cnt[i - 1] if i - 1 >= 0 else 0 for i in nums]
                
            
            
            
         
            
            
        
        
        