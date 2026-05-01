class Solution:
    def subarraySum(self, nums, k):
        count = 0
        curr = 0
        prefix = {0:1}
        
        for num in nums:
            curr += num
            if curr - k in prefix:
                count += prefix[curr - k]
            prefix[curr] = prefix.get(curr, 0) + 1
        
        return count