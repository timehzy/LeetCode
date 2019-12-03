#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (35.87%)
# Likes:    263
# Dislikes: 0
# Total Accepted:    27.5K
# Total Submissions: 75.9K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 
# 示例 1:
# 
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 
# 示例 2:
# 
# 输入: coins = [2], amount = 3
# 输出: -1
# 
# 说明:
# 你可以认为每种硬币的数量是无限的。
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    #bfs
    # def coinChange(self, coins: [int], amount: int) -> int:
    #     if amount < 1: return 0
    #     queue = []
    #     for coin in coins: queue.append((coin, 1))

    #     while queue:
    #         cur, count = queue.pop(0)
    #         if cur == amount: return count
    #         for coin in coins:
    #             if cur + coin <= amount and (cur + coin, count + 1) not in queue : 
    #                 queue.append((cur + coin, count + 1))
    #                 # visited.add(cur)
    #     return -1

    # dp
    # def coinChange(self, coins: [int], amount: int) -> int:
    #     dp = [0] + [float('inf')]*amount
    #     for c in coins:
    #         for i in range(c, amount + 1):
    #             dp[i] = min(dp[i], dp[i - c] + 1)
    #     return -1 if dp[-1] == float('inf') else dp[-1]

    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [0] + [float('inf')]*amount
        for c in coins:
            for i in range(c, amount+1):
                dp[i] = min(dp[i], dp[i - c]+1)
        return -1 if dp[-1] == float('inf') else dp[-1]

print(Solution().coinChange([1,2,5],100))
# @lc code=end

