#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (51.03%)
# Likes:    643
# Dislikes: 0
# Total Accepted:    101.6K
# Total Submissions: 197K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 
# 注意你不能在买入股票前卖出股票。
# 
# 示例 1:
# 
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 
# 
# 示例 2:
# 
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        # 初始状态，因为没有买入，所以卖出的利润是0；
        # 当开始交易时，买入价格越低越好，所以初始设置为最大数
        sold_out, buy_in = 0, float('-inf')
        for n in prices:
            # 最大利润的卖出价格是前一天价格卖出和今天价格卖出的较大值。
            # 今天卖出利润就是今天的价格减去买入价
            sold_out = max(sold_out, n + buy_in)
            # 买入价格越低越好，所以是前一天买入价格和今天买入价格的较小值
            buy_in = max(buy_in, -n)
        return sold_out
# @lc code=end

