from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def move(s, e):
            key_index = s
            key_value = nums[key_index]
            while s < e:
                while s < e and nums[e] > key_value:
                    e -= 1
                while s < e and nums[s] <= key_value:
                    s += 1
                swap(nums, s, e)
            swap(nums, key_index, e)
            return e

        def quickSort(nums, s, e):
            if e - s >= 1:
                mid = move(s, e)
                quickSort(nums, s, mid-1)
                quickSort(nums, mid+1, e)

        quickSort(nums, 0, len(nums)-1)
        return nums


if __name__ == '__main__':
    array = [5,1,1,2,0,0]
    so = Solution()
    print(so.sortArray(array))