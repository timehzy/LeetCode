#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (28.44%)
# Likes:    386
# Dislikes: 0
# Total Accepted:    27.6K
# Total Submissions: 96.3K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 
# 示例 1:
# 
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
# 
# 示例 2:
# 
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# 
#

# @lc code=start
class Solution:
    # 思路：遍历字符，如果是“(”肯定不能成为最后一个有效括号，所以只看从第二个字符开始是")"的。如果前一个字符是“(”，那么可以是有效括号，这是这个字符为结尾的最长有效括号就是其上上一个字符的最长有效长度+2。另一种情况就是虽然前一个是“)”，但如果这个")"为结尾但最长有效括号开头的那个字符的前一个字符是“(”，这样的情况也是有效的。这时最长有效长度就是前一个字符为结尾的最长有效长度+2，再加前一段最长的有效长度。
    def longestValidParentheses(self, s: str) -> int:
        dp, res = [0] * len(s), 0
        for i in range(len(s)):
            if i > 0 and s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif (i - dp[i - 1] - 1 >= 0) and (s[i - dp[i - 1] - 1] == "("):
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if res < dp[i]: res = dp[i]
        return res





# @lc code=end