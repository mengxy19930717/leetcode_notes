from typing import List
import math

class Solution:

    def climbStairs(self, n: int) -> int:
        res = [0, 1, 2]
        for i in range(3, n+1):
            res.append(res[i-2] + res[i-1])
        return res[n]


    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0]
        dp.append(nums[0])
        for i in range(2, size+1):
            dp.append(max(dp[i-2] + nums[i-1], dp[i-1]))
        return dp[size]


    def rob2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob(nums[1:]), self.rob(nums[:-1]))


    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[10000 for _ in range(col+1)] for _ in range(row+1)]
        dp[0][1] = 0
        for i in range(1,row+1):
            for j in range(1,col+1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        return dp[row][col]


    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        size = len(nums)
        res = 0
        i = 2
        while i < size:
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                difference = nums[i] - nums[i-1]
                dp = 1
                i += 1
                add = 2
                while i < size and nums[i] - nums[i-1] == difference:
                    dp += add
                    add += 1
                    i += 1
                res += dp
            i += 1
        return res


    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        if n == 3:
            return 2
        dp = [i for i in range(n+1)]
        for i in range(3, n+1):
            for j in range(1, int(i / 2)+1):
                dp[i] = max(dp[j] * dp[i-j], dp[i])
        print(dp)
        return dp[n]


    #比较秀，多看看
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = i
            for j in range(int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]


    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1 for i in range(size)]
        for i in range(1, size):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


    def wiggleMaxLength(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [[1 for _ in range(size)] for _ in range(2)]
        max_num = 1
        for i in range(1, size):
            for j in range(0, i):
                if nums[i] < nums[j]:
                    dp[0][i] = max(dp[0][i], dp[1][j] + 1)
                    max_num = max(dp[0][i], max_num)
                else:
                    dp[1][i] = max(dp[1][i], dp[0][j] + 1)
                    max_num = max(dp[1][i], max_num)
        return max_num


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        size1 = len(text1)
        size2 = len(text2)
        dp = [[0 for _ in range(size2+1)] for _ in range(size1+1)]

        for i in range(1,size1+1):
            for j in range(1,size2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[size1][size2]


    #背包问题基础题，好好看
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        half = int(sum(nums) / 2)
        size = len(nums)
        dp = [False for _ in range(half+1)]
        if nums[0] <= half:
            dp[nums[0]] = True
        dp[0] = True

        for i in range(1, size):
            for j in range(half, nums[i], -1):
                dp[j] = dp[j] or dp[j-nums[i]]
                if dp[half] == True:
                    return True
        return dp[half]


    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        length = sum(nums)
        if S > length or S < -length:
            return -1
        size = len(nums)
        dp = [[0 for _ in range(2 * length + 1)] for _ in range(size)]
        dp[0][nums[0] + length] = 1
        dp[0][-nums[0] + length] += 1

        for i in range(1, size):
            for j in range(2 * length + 1):
                l, r = 0, 0
                if j - nums[i] >= 0:
                    l = dp[i][j-nums[i]]
                if j + nums[i] < 2 * length + 1:
                    r = dp[i-1][j+nums[i]]
                dp[i][j] = l + r
        return dp[size-1][S+length]


    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        size = len(strs)
        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(size+1)]
        def get_num(num_str):
            res = [0, 0]
            for s in num_str:
                if s == '0':
                    res[0] += 1
                elif s == '1':
                    res[1] += 1
            return res


        for i in range(1, size+1):
            for j in range(0, m+1):
                for k in range(0, n+1):
                    ms = get_num(strs[i-1])[0]
                    ns = get_num(strs[i-1])[1]
                    dp[i][j][k] = dp[i-1][j][k]
                    if j >= ms and k >= ns:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-ms][k-ns] + 1)
        return dp[size][m][n]


    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        size = len(coins)
        dp = [10000 for _ in range(amount+1)]
        coins.sort()
        dp[0] = 0

        for i in range(0, size):
            for j in range(amount, 0, -1):
                for k in range(int(j/coins[i]), , -1):
                    value = dp[j-k*coins[i]]+k
                    dp[j] = min(dp[j], value)
        if dp[amount] == 10000:
            return -1
        return dp[amount]


    #最长回文子串
    def longestPalindrome(self, s: str) -> str:
        maxLength = 1
        index = [0, 0]
        size = len(s)
        dp = [[False for _ in range(size)] for _ in range(size)]
        for i in range(size):
            dp[i][i] = True
        for i in range(size-1, -1, -1):
            for j in range(i+1, size):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1 > maxLength:
                    maxLength = j-i+1
                    index[0], index[1] = i, j
        return s[index[0]:index[1]+1]



if __name__ == '__main__':
    so = Solution()
    print(so.coinChange([186,419,83,408],6249))
