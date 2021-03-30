from typing import List


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.append(nums.pop(i))


    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(nums)
        col = len(nums[0])
        if row * col != r * c:
            return nums
        matrix = [[0 for i in range(c)] for i in range(r)] #二维矩阵初始化

        for i in range(r):
            for j in range(c):
                matrix[i][j] = nums[int((i*c+j)/col)][(i*c+j)%col]
        return matrix


    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0
        i = 0
        while i < len(nums):
            tmp = 0
            while i < len(nums) and nums[i] == 1:
                tmp += 1
                i += 1
            max1 = max(max1, tmp)
            i += 1
        return max1


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) - 1
        j = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False


    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pass



    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                res.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res











if __name__ == '__main__':
    a = [0,0,1]
    so = Solution()
    so.moveZeroes(a)
    nums =[1,2,2,3,4,6]
    #so.findErrorNums(nums)
    print(so.findErrorNums(nums))