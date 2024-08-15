class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        numbers = set(nums) 
        for num in nums:
                if num + diff in numbers and num + 2 * diff in numbers:
                    count += 1
        return count
      
                
        