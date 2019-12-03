#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (31.20%)
# Likes:    148
# Dislikes: 0
# Total Accepted:    54.1K
# Total Submissions: 171.3K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 
# 如果不存在最后一个单词，请返回 0 。
# 
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 
# 示例:
# 
# 输入: "Hello World"
# 输出: 5
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word, length = False, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and word == True: return length
            if s[i] != " ": word = True; length += 1
        return length if word else 0

# @lc code=end

