from typing import List

class Solution:

    #挺有意思的括号匹配
    def isValid(self, s: str) -> bool:
        s = s.strip()
        if len(s) == 0:
            return True
        s = list(s)
        standard_dict = {'[':']', '(':')', '{':'}'}
        stack = []
        while len(s) != 0 or len(stack) != 0:
            if len(s) == 0 and len(stack) != 0:
                return False
            tmp = s.pop(0)
            if len(stack) == 0:
                stack.append(tmp)
                continue
            else:
                if standard_dict.get(stack[-1]) == tmp:
                    stack.pop()
                else:
                    stack.append(tmp)
        return True


    #这题也没想出来，构建递减栈
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        stack.append([0,T.pop(0)])
        for i in range(1, len(T)+1):
            tmp = T.pop(0)
            while len(stack) != 0 and tmp > stack[-1][1]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i, tmp])
        return res


    #
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        nums = nums + nums
        length = len(nums)
        res = [-1] * length
        stack = []
        stack.append([0,nums.pop(0)])
        for i in range(1, length):
            tmp = nums.pop(0)
            while len(stack) != 0 and tmp > stack[-1][1]:
                res[stack[-1][0]] = tmp
                stack.pop()
            stack.append([i,tmp])
        return res[:int(length/2)]


if __name__ == '__main__':
    a = [55,38,53,81,61,93,97,32,43,78]
    so = Solution()
    print(so.nextGreaterElements(a))




