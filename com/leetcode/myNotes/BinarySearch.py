from typing import List

class Solution:

    def mySqrt(self, x: int) -> int:
        l = 0
        h = x
        while l <= h:
            mid = l + int((h - l) / 2)
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                h = mid - 1
            else:
                l = mid + 1
        return h


    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        l = 0
        h = length - 1
        key = nums[-1]
        while l < h:
            mid = l + int((h - l) / 2)
            if nums[mid] > key:
                l = mid + 1
            else:
                h = mid
        return nums[l]