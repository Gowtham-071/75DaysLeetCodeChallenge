class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                curr = num
                count = 1

                while curr + 1 in s:
                    curr += 1
                    count += 1

                longest = max(longest, count)

        return longest