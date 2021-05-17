from typing import List
import heapq
from com.leetcode.myNotes.TreeNodeAlgorithm import TreeNode
from com.leetcode.myNotes.ListNodeAlgorithm import ListNode


#小顶堆实现 ---- 大顶堆可根据小顶堆改
class Myheap():
    def __init__(self, k):
        self.data = []
        self.k = k

    def push(self, element):
        if len(self.data) < self.k:
            heapq.heappush(self.data, element)
        else:
            if element > self.data[0]:
                heapq.heappop(self.data)
                heapq.heappush(self.data, element)

class Solution():
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Myheap(k)
        for num in nums:
            heap.push(num)
        return heap.data[0]


    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        cur = [root]
        next = []
        reverse_flag = 0
        def nodeListVal(listTreeNode):
            val_list = []
            for node in listTreeNode:
                val_list.append(node.val)
            return val_list
        while len(cur) != 0 or len(next) != 0:
            if reverse_flag % 2 == 0:
                res.append(nodeListVal(cur))
            else:
                res.append(nodeListVal(reversed(cur)))
            for node in cur:
                if node.left is not None:
                    next.append(node.left)
                if node.right is not None:
                    next.append(node.right)
            cur = next
            next = []
            reverse_flag += 1
        return res


    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1 for _ in range(size)]
        max_length = 1
        for i in range(1, size):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_length = max(dp[i], max_length)
        return max_length


    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        val = preorder[0]
        root = TreeNode(val)
        mid_inorder_index = inorder.index(val)
        #mid_preorder_index = preorder.index(inorder[mid_inorder_index-1])
        root.left = self.buildTree(preorder[1:mid_inorder_index+1], inorder[:mid_inorder_index])
        root.right = self.buildTree(preorder[mid_inorder_index+1:], inorder[mid_inorder_index+1:])
        return root


    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        def merge(alist, blist):
            sizea = len(alist)
            sizeb = len(blist)
            i = 0
            j = 0
            nonlocal res
            merge_list = []
            while i < sizea and j < sizeb:
                if alist[i] <= blist[j]:
                    merge_list.append(alist[i])
                    i += 1
                    res += j
                else:
                    merge_list.append(blist[j])
                    j += 1
            if i == sizea:
                merge_list += blist[j:]
            elif j == sizeb:
                merge_list += alist[i:]
                res += (sizea - i) * sizeb
            return merge_list

        def merge_sort(nums, s, e):
            if e - s <= 1:
                return nums[s:e]
            mid = s + int((e - s) / 2)
            left = merge_sort(nums, s, mid)
            right = merge_sort(nums, mid, e)
            nonlocal res
            return merge(left, right)

        merge_sort(nums, 0, len(nums))
        return res


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        res = []
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1
        while True:
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break
            for i in range(t, b+1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                break
            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pass

    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        maxprofit = 0
        for price in prices:
            if price <= min_value:
                min_value = price
            else:
                maxprofit = max(maxprofit, price-min_value)
        return maxprofit

if __name__ == '__main__':
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    so = Solution()
    print(so.spiralOrder(nums))