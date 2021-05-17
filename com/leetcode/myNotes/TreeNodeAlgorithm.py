from typing import List
import math

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and \
               abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1


    #这个题也想了好久，主要是不知道如何引入变量diameter以及公式嵌套的使用，关注！！！
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        def Depth(root):
            if not root:
                return 0
            left = Depth(root.left)
            right = Depth(root.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1
        Depth(root)
        return self.diameter

    #也写错了，先计算出left,right再赋值，先赋值的话树结构就改变了
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root


    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    #根节点是最顶上的那个
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        return (targetSum - root.val == 0 and not root.left and not root.right) \
               or self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)


    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return
            pathSum(root, sum)
            dfs(root.left)
            dfs(root.right)

        def pathSum(root, sum):
            if not root:
                return
            if sum - root.val == 0:
                self.res += 1
            pathSum(root.left, sum-root.val)
            pathSum(root.right, sum-root.val)
        dfs(root)
        return self.res


    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        self.flag = False

        def dfs(s, t):
            if not s:
                return
            if s.val == t.val and not self.flag:
                if sameTree(s, t):
                    self.flag = True
                    return
            dfs(s.left, t)
            dfs(s.right, t)
            return

        def sameTree(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and sameTree(t1.left, t2.left) and sameTree(t1.right, t2.right)

        dfs(s, t)
        return self.flag


    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric(root1: TreeNode, root2: TreeNode):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return root1.val == root2.val and symmetric(root1.left, root2.right) and symmetric(root1.right, root2.left)
        return symmetric(root, root)


    #可是真没做出来，多看看题解吧
    #is not xx 和 not xx 不等价，root.left is not None 可以 但是if not root.left 不可以 尽量使用is not None来判定None
    '''
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        self.univaluePath(root)
        return self.ans


    def univaluePath(self, root:TreeNode):
        if not root:
            return 0
        left = self.univaluePath(root.left)
        right = self.univaluePath(root.right)
        left = left + 1 if root.left is not None and root.val == root.left.val else 0
        right = right + 1 if root.right is not None and root.val == root.right.val else 0
        self.ans = max(self.ans, left + right)
        return max(left, right)
    '''

    def longestUnivaluePath(self, root: TreeNode) -> int:
        pass


    #耗时太长，方法是对的
    def rob(self, root: TreeNode) -> int:
        self.ans = 0
        self.robScore(root)
        return self.ans

    def robScore(self, root:TreeNode) -> int:
        if not root:
            return 0
        val1 = root.val
        if root.left is not None:
            val1 += self.robScore(root.left.left) + self.robScore(root.left.right)
        if root.right is not None:
            val1 += self.robScore(root.right.left) + self.robScore(root.right.right)
        val2 = self.robScore(root.left) + self.robScore(root.right)
        self.ans = max(self.ans, max(val1, val2))
        return max(val1, val2)


    #竟然一次就对了
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1
        if root.left is None and root.right is None:
            return -1
        if root.val == root.left.val == root.right.val:
            left = self.findSecondMinimumValue(root.left)
            right = self.findSecondMinimumValue(root.right)
        elif root.val == root.left.val and root.val != root.right.val:
            left = self.findSecondMinimumValue(root.left)
            right = root.right.val
        elif root.val != root.left.val and root.val == root.right.val:
            left = root.left.val
            right = self.findSecondMinimumValue(root.right)
        else:
            left = root.left.val
            right = root.right.val

        if left == right and (left == -1 or left == root.val):
            return -1
        if left > 0 and right > 0:
            return min(left, right)
        if left < 0 or right < 0:
            return max(left, right)


    #这题第一遍做错了，也是醉了。1、cur、next任何一个非空都可以执行 2、cur = next后要对next还原
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        cur = []
        cur.append(root)
        while len(cur) != 0 or len(next) != 0:
            tmp = []
            next = []
            while len(cur) != 0:
                node = cur.pop()
                tmp.append(node.val)
                if node.left is not None:
                    next.append(node.left)
                if node.right is not None:
                    next.append(node.right)
            res.append(sum(tmp) / len(tmp))
            cur = next
        return res


    def findBottomLeftValue(self, root: TreeNode) -> int:
        cur = []
        next = []
        cur.append(root)
        while len(cur) != 0 or len(next) != 0:
            res = cur[0].val
            next = []
            while len(cur) != 0:
                node = cur.pop(0)
                if node.left is not None:
                    next.append(node.left)
                if node.right is not None:
                    next.append(node.right)
            cur = next
        return res


    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        cur = [root]
        while len(cur) != 0:
            node = cur.pop()
            res.append(node.val)
            if node.right is not None:
                cur.append(node.right)
            if node.left is not None:
                cur.append(node.left)
        return res


    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root is None:
            return root
        if root.val < low:
            root = self.trimBST(root.right, low, high)
        elif root.val > high:
            root = self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root


    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.list = []
        self.midOrder(root)
        return self.list[k-1]

    def midOrder(self, root):
        if root is None:
            return
        self.midOrder(root.left)
        self.list.append(root.val)
        self.midOrder(root.right)


    def convertBST(self, root: TreeNode) -> TreeNode:
        self.num = 0
        root = self.bst(root)
        return root

    def bst(self, root) -> TreeNode:
        if root is None:
            return root
        self.bst(root.right)
        tmp = root.val
        root.val += self.num
        self.num += tmp
        self.bst(root.left)
        return root


    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor1(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor1(root.left, p, q)
        else:
            return root


    #记住递归条件，走到p,q也不走了
    #这题理解与上述题不太一样，后续遍历，从下到上找p,q。递归函数是找pq。而不是找p、q的公共节点
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right


    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        mid = math.ceil(len(nums) / 2) - 1
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


    #链表的题要考虑断开连接
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        low = head
        fast = head
        pre = low
        while fast is not None and fast.next is not None:
            pre = low
            low = low.next
            fast = fast.next.next
        root = TreeNode(low.val)
        next = low.next
        low.next = None
        pre.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(next)
        return root


    














if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    s = Solution()
    print(s.longestUnivaluePath((a)))
