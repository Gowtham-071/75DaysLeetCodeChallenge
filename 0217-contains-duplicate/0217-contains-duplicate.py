class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        view = set()
        for num in nums:
            if num in view:
                return True
            view.add(num)
        return False