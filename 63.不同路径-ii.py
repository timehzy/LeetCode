#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
# https://leetcode-cn.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (31.79%)
# Likes:    179
# Dislikes: 0
# Total Accepted:    28.8K
# Total Submissions: 90.4K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 
# 
# 
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 
# 说明：m 和 n 的值均不超过 100。
# 
# 示例 1:
# 
# 输入:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 
# 
#

# @lc code=start
class Solution:
    # def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
    #     if not obstacleGrid: return 0
    #     r, c = len(obstacleGrid), len(obstacleGrid[0])
    #     dp = [[0 for _ in range(c)] for _ in range(r)]
    #     dp[0][0] = 1 - obstacleGrid[0][0] # 第一个位置的路径
    #     # 第一列的路径是当上面的块无障碍（0）且当前的块无障碍（0），否则就不通（1）。用乘法巧妙的计算，第一行也是同样的情况
    #     for i in range(1, r):
    #         dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
    #     for j in range(1, c):
    #         dp[0][j] = dp[0][j-1] * (1 - obstacleGrid[0][j])
    #     # 计算路径和，左侧和上侧的路径相加，但是如果当前路径是障碍则归0，同样是乘法来巧妙的解决
    #     for i in range(1, r):
    #         for j in range(1, c):
    #                 dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (1 - obstacleGrid[i][j])
    #     return dp[-1][-1]

    # def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
    #     if not obstacleGrid: return 0
    #     r, c = len(obstacleGrid), len(obstacleGrid[0])
    #     dp = [[0 for _ in range(c)] for _ in range(r)]
    #     dp[0][0] = 1 - obstacleGrid[0][0] # 第一个位置的路径
    #     # 第一列的路径是当上面的块无障碍（0）且当前的块无障碍（0），否则就不通（1）。用乘法巧妙的计算，第一行也是同样的情况
    #     # for i in range(1, r):
    #     #     dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
    #     # for j in range(1, c):
    #     #     dp[0][j] = dp[0][j-1] * (1 - obstacleGrid[0][j])
    #     # 计算路径和，左侧和上侧的路径相加，但是如果当前路径是障碍则归0，同样是乘法来巧妙的解决
    #     for i in range(0, r):
    #         for j in range(0, c):
    #             if i == 0 and j == 0: continue
    #             elif j == 0:
    #                 dp[i][j] = dp[i-1][j] * (1 - obstacleGrid[i][j])
    #             elif i == 0:
    #                 dp[i][j] = dp[i][j-1] * (1 - obstacleGrid[i][j])
    #             else:
    #                 dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (1 - obstacleGrid[i][j])
    #     return dp[-1][-1]

    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        if not obstacleGrid: return 0
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0][0] = 1 - obstacleGrid[0][0] # 第一个位置的路径
        for i in range(0, r):
            for j in range(0, c):
                if i == 0 and j == 0: continue
                top, left = 0 if i == 0 else dp[i-1][j], 0 if j == 0 else dp[i][j-1]
                dp[i][j] = (top + left) * (1 - obstacleGrid[i][j])
        return dp[-1][-1]

# @lc code=end

