class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            right = [0] * len(nums)
            right[-1] = nums[-1]

            for i in range(1, len(nums)):
                right[len(nums)-i-1] = right[len(nums)-i] * nums[len(nums)-i-1]

            res = [0] * len(nums)
            left = 1
            idx = 0

            while idx < len(res) - 1:
                res[idx] = left * right[idx + 1]
                left *= nums[idx]
                idx += 1

            res[-1] = left
            return res

        