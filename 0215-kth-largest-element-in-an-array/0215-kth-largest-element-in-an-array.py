import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -= 1

        def quickselect(l, r):
            pivot = nums[random.randint(l, r)]

            left = l
            mid = l
            right = r

            while mid <= right:
                if nums[mid] > pivot:
                    nums[left], nums[mid] = nums[mid], nums[left]
                    left += 1
                    mid += 1

                elif nums[mid] < pivot:
                    nums[mid], nums[right] = nums[right], nums[mid]
                    right -= 1

                else:
                    mid += 1

            if k < left:
                return quickselect(l, left - 1)

            elif k > right:
                return quickselect(right + 1, r)

            return pivot

        return quickselect(0, len(nums) - 1)