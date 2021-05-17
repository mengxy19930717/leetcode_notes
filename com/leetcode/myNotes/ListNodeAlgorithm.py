class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

def listNodePrint(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    curA = headA
    curB = headB
    while curA is not curB:
        curA = headB if curA is None else curA.next
        curB = headA if curB is None else curB.next
    return curA


def reverseList(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    cur = head
    next = None
    while cur is not None:
        tmp = cur.next
        cur.next = next
        next = cur
        cur = tmp
    return next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    head = ListNode(-1)
    cur = head
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 if l2 is None else l2
    return head.next


def swapPairs(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    head_fake = ListNode(-1)
    head_fake.next = head
    pre = head_fake
    while head is not None and head.next is not None:
        tmp = head.next.next
        pre.next = head.next
        head.next = None #断链，要不链有循环
        pre.next.next = head
        pre = pre.next.next
        head = tmp
    pre.next = head #考虑奇数情况
    return head_fake.next
    

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    list1, list2 = [], []
    while l1 is not None:
        list1.append(l1.val)
        l1 = l1.next
    while l2 is not None:
        list2.append(l2.val)
        l2 = l2.next
    pre = None
    carry = 0
    while len(list1) != 0 or len(list2) != 0 or carry != 0:
        value1 = list1.pop() if len(list1) != 0 else 0
        value2 = list2.pop() if len(list2) != 0 else 0
        value = value1 + value2
        number = (value + carry) % 10
        carry = int((value + carry) / 10)
        cur = ListNode(number)
        cur.next = pre
        pre = cur
    return cur

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(3)
    f = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    #d.next = e
    #e.next = f
    listNodePrint(swapPairs(a))
