from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}
        for i in range(len(nums)):
            if nums[i] not in dict_num: #判断dict里是否包含nums[i]的key
                dict_num[target - nums[i]] = i
            else:
                return [i, dict_num[nums[i]]]


    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_num = {}
        for i in range(len(nums)):
            if nums[i] in dict_num:
                return True
            else:
                dict_num[nums[i]] = 1
        return False


    def findLHS(self, nums: List[int]) -> int:
        dict_num = defaultdict(int)
        for i in range(len(nums)):
            dict_num[nums[i]] += 1
            if nums[i] + 1 in nums:
                dict_num[nums[i]+1] += 1
        max_length = 0
        print(dict_num)
        for key, value in dict_num.items():
            if key - 1 in dict_num:
                max_length = max(max_length, value)
        return max_length


    #脑子有点乱，明天想
    def longestConsecutive(self, nums: List[int]) -> int:
        dict_count = defaultdict(int)
        max_length = 0
        for i in range(len(nums)):
            dict_count[nums[i]] += 1
        dict_num = defaultdict(int)
        for key, value in dict_count.items():
            dict_num[key] = dict_count[key] + dict_count[key-1] if key - 1 in dict_count else dict_count[key]
        for key, value in dict_num.items():
            length = dict_num[key-1] + value if key - 1 in dict_num else value
            max_length = max(max_length, length)
        return max_length



if __name__ == '__main__':
    s = [1,3,2,2,5,2,3,7]
    so = Solution()
    so.findLHS(s)
