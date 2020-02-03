#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
# https://leetcode-cn.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (33.29%)
# Likes:    99
# Dislikes: 0
# Total Accepted:    9.3K
# Total Submissions: 27.6K
# Testcase Example:  '"aba"'
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
# 
# 示例 1:
# 
# 
# 输入: "aba"
# 输出: True
# 
# 
# 示例 2:
# 
# 
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
# 
# 
# 注意:
# 
# 
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
# 
# 
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str, recur=True) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]: l += 1; r -= 1; continue
            if not recur: return False
            return self.validPalindrome(s[l+1:r+1], False) or self.validPalindrome(s[l:r], False)
        return True

# @lc code=end

