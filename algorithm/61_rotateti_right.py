"""

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""

"""
思路：将链表值取到列表中，移动然后重新创建新的链表
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k == 0: return head
        t1 = head
        result = []
        count = 0
        while t1 is not None:
            count += 1
            result.append(t1.val)
            t1 = t1.next
        if k % count == 0:
            return head
        k = k % count
        result = result[-k:] + result[:-k]
        return result
        cul = ListNode(0)
        pre = cul
        for i in result:
            node = ListNode(i)
            pre.next = node
            pre = pre.next
        return cul.next
