#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (48.72%)
# Likes:    538
# Dislikes: 0
# Total Accepted:    77.9K
# Total Submissions: 158.4K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def isMirror(t1: TreeNode, t2: TreeNode) -> bool:
    #         if not t1 and not t2: return True
    #         if not t1 or not t2: return False
    #         return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
    #     return isMirror(root, root)

    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root, root]
        while queue:
            left, right = queue.pop(0), queue.pop(0)
            if not left and not right: continue
            if not left or not right: return False
            if left.val != right.val: return False
            for node in (left.left, right.right, left.right, right.left):
                queue.append(node)
        return True

            
# @lc code=end

