#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (21.86%)
# Likes:    222
# Dislikes: 0
# Total Accepted:    21.9K
# Total Submissions: 99.1K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 
# 示例 1:
# 
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2:
# 
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == "0" : return 0
        dp = [1]*len(s)
        for i in range(1, len(s)):
            if s[i] == "0" and s[i - 1] == "0": return 0
            if "0" < s[i] < "7" and "0" < s[i - 1] < "3": 
                dp[i] = dp[i - 1] + 1
            else: 
                dp[i] = dp[i - 1]
        return dp[-1]

# print(Solution().numDecodings("10"))
# @lc code=end

