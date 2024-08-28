class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        differenceArray = [0] * n
        leftSum = 0
        rightSum = sum(nums)
        for i in range(n):
            rightSum -= nums[i]
            differenceArray[i] = abs(rightSum - leftSum)
            leftSum += nums[i]

        return differenceArray