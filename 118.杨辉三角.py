#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (64.20%)
# Likes:    215
# Dislikes: 0
# Total Accepted:    51.2K
# Total Submissions: 78.7K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> [[int]]:
        res = []
        for i in range(0, numRows):
            t = [0] * (i+1)
            t[0] = t[-1] = 1
            for j in range(1, i):
                t[j] = res[i-1][j-1] + res[i-1][j]
            res.append(t)
        return res
        
# @lc code=end

