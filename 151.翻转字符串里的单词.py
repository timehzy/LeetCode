#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (31.88%)
# Likes:    91
# Dislikes: 0
# Total Accepted:    23.6K
# Total Submissions: 70.8K
# Testcase Example:  '"the sky is blue"'
#
# 给定一个字符串，逐个翻转字符串中的每个单词。
# 
# 
# 
# 示例 1：
# 
# 输入: "the sky is blue"
# 输出: "blue is sky the"
# 
# 
# 示例 2：
# 
# 输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 
# 
# 示例 3：
# 
# 输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
# 
# 
# 
# 
# 说明：
# 
# 
# 无空格字符构成一个单词。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
# 
# 
# 
# 
# 进阶：
# 
# 请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。
# 
#

# @lc code=start
class Solution:
    # 极简三行
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        sarr = s.split()
        return " ".join(sarr[::-1])

    # def reverseWords(self, s: str) -> str:
    #     # 过滤两头的空格，并将每个单词作为元素存储在数组中
    #     start = 0
    #     while start < len(s) and s[start] == " ": start += 1
    #     s = s[start:]

    #     end = len(s) - 1 
    #     while end >= 0 and s[end] == " ": end -= 1
    #     s, sarr, start = s[:end+1], [], 0

    #     while start < len(s):
    #         end = start
    #         while end < len(s) and s[end] != " ": end += 1
    #         sarr.append(s[start:end])
    #         start = end+1
    #         while start < len(s) and s[start] == " ": start += 1

    #     result = ""
    #     for word in reversed(sarr):
    #         result += word + " "
    #     return result[:-1]



print(Solution().reverseWords(" "))


# @lc code=end

