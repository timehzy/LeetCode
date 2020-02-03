#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (31.64%)
# Likes:    2525
# Dislikes: 0
# Total Accepted:    234.6K
# Total Submissions: 741.6K
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# @lc code=start
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     res, cset = 0, set()
    #     for i in range(len(s)):
    #         for j in range(i, len(s)):
    #             if s[j] not in cset: cset.add(s[j])
    #             else: break
    #         if len(cset) > res: res = len(cset)                    
    #         cset.clear()
    #     return res
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     i, j, length, cset, res = 0, 0, len(s), set(), 0
    #     while i < length and j < length:
    #         if s[j] not in cset:
    #             cset.add(s[j])
    #             j += 1
    #             res = max(res, j - i)
    #         else:
    #             cset.remove(s[i])
    #             i += 1
    #     return res
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, res, dic = 0, 0, {}
        for j in range(len(s)):
            if s[j] in dic: i = max(dic[s[j]], i)
            res = max(res, j - i + 1)
            dic[s[j]] = j + 1
        return res

# print(Solution().lengthOfLongestSubstring("pwwkew"))
# @lc code=end

