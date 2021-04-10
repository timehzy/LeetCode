#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (54.79%)
# Likes:    1248
# Dislikes: 0
# Total Accepted:    240.9K
# Total Submissions: 439.6K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
# 
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 
# 
# 示例 2：
# 
# 输入：lists = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：lists = [[]]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
# 
# 
#
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 第一次做，没有想太多，直接每次遍历所有链表，找最小的，虽然通过，但是只击败了8%哈哈，毕竟是O(n*k),n是所有链表的节点个数，k是链表的个数，效率很低。看了题解，可以用归并的做法，非常巧妙。
    # def mergeKLists(self, lists: [ListNode]) -> ListNode:
    #     cur = []
    #     for l in lists:
    #         if l != None: cur.append(l)
    #     res, ans = None, None
    #     while len(cur) > 0:
    #         curMin = cur[0]
    #         curMinIndex = 0
    #         for i in range(1, len(cur)): 
    #             if cur[i].val < curMin.val:
    #                 curMin = cur[i]
    #                 curMinIndex = i
    #         if curMin.next:
    #             cur[curMinIndex] = curMin.next
    #         else:
    #             cur.remove(curMin)

    #         if res:
    #             res.next = curMin
    #             res = res.next
    #         else:
    #             res = curMin
    #             ans = res
    #     return ans
    def mergeKLists(self, lists: [ListNode]) -> ListNode:

        def mergeTowList(l1, l2):
            if not l1: return l2
            if not l2: return l1
            if l1.val < l2.val:
                l1.next = mergeTowList(l1.next, l2)
                return l1
            else:
                l2.next = mergeTowList(l1, l2.next)
                return l2

        def merge(l, r):
            if l == r: return lists[l]
            m = l + ((r - l) // 2)
            l1 = merge(l, m)
            l2 = merge(m+1, r)
            return mergeTowList(l1, l2)

        if not lists: return
        return merge(0, len(lists)-1)    

# a = ListNode(1, ListNode(4, ListNode(5)))
# b = ListNode(1, ListNode(3, ListNode(4)))
# c = ListNode(2, ListNode(6))
# print(Solution().mergeKLists([a,b,c]))
# @lc code=end

