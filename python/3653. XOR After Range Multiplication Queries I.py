class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for left, right, inc, val in queries:
            for idx in range(left, right + 1, inc):
                nums[idx] = (nums[idx] * val) % (10**9 + 7)

        res = 0
        for num in nums:
            res ^= num

        return res
