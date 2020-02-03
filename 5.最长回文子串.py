#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.37%)
# Likes:    1354
# Dislikes: 0
# Total Accepted:    121.3K
# Total Submissions: 443.2K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        start = end = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if i == j: continue
                ht = s[i] == s[j]
                inner = dp[i+1][j-1] if (i + 1) <= (j - 1) else True
                dp[i][j] = inner and ht
                if dp[i][j] and (j - i) > (end - start): 
                    start = i; end = j
        return s[start:end+1]

                    
print(Solution().longestPalindrome("babcccc"))

# @lc code=end

