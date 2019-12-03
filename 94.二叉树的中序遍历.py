#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (68.30%)
# Likes:    300
# Dislikes: 0
# Total Accepted:    68.6K
# Total Submissions: 100.2K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     res = []

    #     def helper(root: TreeNode):
    #         if not root: return
    #         helper(root.left)
    #         res.append(root.val)
    #         helper(root.right)
        
    #     helper(root)
    #     return res

    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     stack, res = [], []
    #     p = root
    #     while p or stack:
    #         while p:
    #             stack.append(p)
    #             p = p.left
    #         p = stack.pop()
    #         res.append(p.val)
    #         p = p.right
    #     return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res, p = [root], [], root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            res.append(p.val)
            p = p.right
        return res



# @lc code=end
