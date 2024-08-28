class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        result = 0
        for x in c:
            if x + 1 in c:
                result = max(result, c[x] + c[x + 1])
        return result