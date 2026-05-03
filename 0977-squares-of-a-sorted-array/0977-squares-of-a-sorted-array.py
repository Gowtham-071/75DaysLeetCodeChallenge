class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        i = n - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l] * nums[l]
                l += 1
            else:
                res[i] = nums[r] * nums[r]
                r -= 1
            i -= 1

        return res