class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        arr = nums
        arr.sort()
        ans = []

        for idx in range(len(arr)):
            if idx > 0 and arr[idx] == arr[idx-1]:
                continue

            left = idx + 1
            right = len(arr) - 1

            while left < right:
                total = arr[idx] + arr[left] + arr[right]

                if total == 0:
                    ans.append([arr[idx], arr[left], arr[right]])

                    left += 1
                    right -= 1

                    while left < right and arr[left] == arr[left-1]:
                        left += 1

                    while left < right and arr[right] == arr[right+1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return ans