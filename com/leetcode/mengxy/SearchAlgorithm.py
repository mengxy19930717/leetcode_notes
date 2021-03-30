from typing import List
from com.leetcode.mengxy.ListNodeAlgorithm import ListNode

class Solution:

    def numSquares(self, n: int) -> int:
        visited = [False for i in range(n + 1)]
        res = 0
        squares = self.generator_square(n)
        cur_process = [n]
        while len(cur_process) != 0:
            next_process = []
            res += 1
            for i in range(len(cur_process)):
                difference = cur_process.pop(0)
                for square in squares:
                    tmp = difference - square
                    if tmp == 0:
                        return res
                    elif tmp > 0 and visited[tmp] is not True:
                        visited[tmp] = True
                        next_process.append(tmp)
                    elif tmp < 0:
                        break
            cur_process = next_process
        return res

    def generator_square(self, n) -> List:
        res = []
        for i in range(1, int(n / 2) + 1):
            if i * i <= n:
                res.append(i * i)
        return res

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        visited = [[[False] for i in range(column)] for j in range(row)]
        max_area = 0

        def areaOfIsland(i: int, j: int):
            if i < 0 or i >= row or j < 0 or j >= column or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            left = areaOfIsland(i - 1, j)
            right = areaOfIsland(i + 1, j)
            top = areaOfIsland(i, j - 1)
            down = areaOfIsland(i, j + 1)
            return 1 + left + right + top + down

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1 and visited[i][j] is not False:
                    visited[i][j] = True
                    max_area = max(max_area, areaOfIsland(i, j))
        return max_area


    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        column = len(board[0])

        def fill(i, j):
            if i < 0 or i >= row or j < 0 or j >= column or board[i][j] == 'X' or board[i][j] == 'Q':
                return
            board[i][j] = 'Q'
            fill(i-1, j)
            fill(i+1, j)
            fill(i, j-1)
            fill(i, j+1)

        for j in range(column):
            if board[0][j] == 'O':
                fill(0, j)
            if board[row-1][j] == 'O':
                fill(row-1, j)
        for i in range(row):
            if board[i][0] == 'O':
                fill(i, 0)
            if board[i][column-1] == 'O':
                fill(i, column-1)
        for i in range(row):
            for j in range(column):
                if board[i][j] == 'Q':
                    board[i][j] = 'O'
                if board[i][j] == 'O':
                    board[i][j] = 'X'


    ##没做出来 重点看
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = [0, 0, 1, -1]
        col = [1, -1, 0, 0]
        board_row = len(board)
        board_col = len(board[0])
        visited = [[False for _ in range(board_col)] for _ in range(board_row)]
        def isExist(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True
            visited[i][j] = True
            for q in range(4):
                tmp_i = i + row[q]
                tmp_j = j + col[q]
                if 0 <= tmp_i < board_row and 0 <= tmp_j < board_col and not visited[tmp_i][tmp_j] \
                        and isExist(tmp_i, tmp_j, k+1):
                    return True

            visited[i][j] = False
            return False

        for i in range(board_row):
            for j in range(board_col):
                if board[i][j] == word[0] and isExist(i, j, 0):
                    return True
        return False

    #树不用标记visited，不会返回
    def binaryTreePaths(self, root) -> List[str]:
        if not root:
            return []
        res = []
        path = []
        def backTrace(root):
            path.append(str(root.val))
            if not root.left and not root.right:
                res.append("->".join(path))
            if root.left:
                backTrace(root.left)
            if root.right:
                backTrace(root.right)
            path.pop(-1)
        backTrace(root)
        return res


    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        visited = [False for i in range(length)]
        res = []
        path = []

        def backTrace():
            if len(path) == length:
                res.append(path.copy())
                print(path)
            for i in range(length):
                if not visited[i]:
                    path.append(nums[i])
                    visited[i] = True
                    backTrace()
                    visited[i] = False
                    path.pop(-1)
        backTrace()
        return res

    #排序后前面有，但还没访问就跳过
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        visited = [False for i in range(length)]
        res = []
        path = []

        def backTrace():
            if len(path) == length:
                res.append(path.copy())
            for i in range(length):
                if i >= 1 and nums[i-1] == nums[i] and not visited[i-1]:
                    pass
                else:
                    if not visited[i]:
                        path.append(nums[i])
                        visited[i] = True
                        backTrace()
                        visited[i] = False
                        path.pop(-1)
        backTrace()
        return res

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        visited = [False for _ in range(n)]
        def backTrace(i_index):
            if len(path) == k:
                res.append(path.copy())
            for i in range(i_index, n+1):
                if not visited[i-1]:
                    visited[i-1] = True
                    path.append(i)
                    backTrace(i+1)
                    path.pop(-1)
                    visited[i-1] = False
        backTrace(1)
        return res


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        size = len(candidates)

        def backTrace(begin, path, target):
            if target == 0:
                res.append(path.copy())
            for i in range(begin, size):
                if target > 0:
                    difference = candidates[i]
                    path.append(difference)
                    backTrace(i, path, target - difference)
                    path.remove(difference)
                else:
                    break
        backTrace(0, [], target)
        return res


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        size = len(candidates)
        visited = [False for _ in range(size)]
        candidates.sort()

        def backTrace(begin, size, target, path):
            if target == 0:
                res.append(path.copy())
            #print(begin)
            for i in range(begin, size):
                if target-candidates[i] < 0:
                    break
                elif i >= 1 and candidates[i-1] == candidates[i] and not visited[i-1]:
                    pass
                else:
                    path.append(candidates[i])
                    visited[i] = True
                    backTrace(i + 1, size, target-candidates[i], path)
                    visited[i] = False
                    path.pop(-1)
        backTrace(0, size, target, [])
        return res


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        size = len(nums)
        visited = [False for _ in range(size)]

        def backTrace(begin, size, path):
            for i in range(begin, size):
                if i >= 1 and nums[i-1] == nums[i] and not visited[i-1]:
                    pass
                else:
                    path.append(nums[i])
                    res.append(path.copy())
                    visited[i] = True
                    backTrace(i+1, size, path)
                    path.pop(-1)
                    visited[i] = False
        backTrace(0, size, [])
        return res





if __name__ == '__main__':
    a = 4
    so = Solution()
    #a = so.combine(4,2)
    b = [['O','O'],['O','O']]
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    #print(so.combinationSum2(candidates, target))
    print(so.subsetsWithDup([1,1,2]))


