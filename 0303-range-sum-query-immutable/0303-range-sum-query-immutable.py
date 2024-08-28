class NumArray:

    def __init__(self, nums: List[int]):        
        self.nums = nums   
        self.dp = [nums[0]]
        for i in range(1, len(nums)):
            self.dp.append(self.dp[-1] + nums[i])
            # sum from 0 to n = n + (sum from 0 to n-1)
        

    def sumRange(self, left: int, right: int) -> int:
        
        return self.nums[left] + self.dp[right] - self.dp[left]