from typing import List
from com.leetcode.mengxy.ListNodeAlgorithm import ListNode
import math


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i, j]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

    def judgeSquareSum(self, c: int) -> bool:
        j = math.floor(math.sqrt(c))
        i = 0
        while i <= j:
            if i * i + j * j == c:
                return True
            elif i * i + j * j > c:
                j -= 1
            else:
                i += 1
        return False

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.palindrome(s, i + 1, j) or self.palindrome(s, i, j - 1)
        return True

    def palindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[k] = nums1[m]
                k -= 1
                m -= 1
            else:
                nums1[k] = nums2[n]
                k -= 1
                n -= 1
        if m < 0:
            for i in range(n + 1):
                nums1[i] = nums2[i]


    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        low = head
        fast = head.next
        while low is not None and fast is not None and fast.next is not None and low != fast:
            low = low.next
            fast = fast.next.next
        if low == fast and low is not None:
            return True
        else:
            return False

