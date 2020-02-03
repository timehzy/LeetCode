#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (38.19%)
# Likes:    181
# Dislikes: 0
# Total Accepted:    12.6K
# Total Submissions: 32K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
# 
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
# 
# 说明：
# 
# 
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
# 
# 
# 示例 1:
# 
# 
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
# 
# 
# 示例 2:
# 
# 
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
# 
# 
#

# @lc code=start
class Solution:

    def countArr(self, s: str) -> [int]:
        arr = [0]*26
        for c in s:
            arr[ord(c) - ord('a')] += 1
        return arr

    def findAnagrams(self, s: str, p: str) -> [int]:
        sa, sp = self.countArr(s[:len(p)]), self.countArr(p)
        res = []
        if sa == sp: res.append(0)
        for i in range(1, len(s)-len(p)+1):
            left = ord(s[i-1])-ord('a')
            right = ord(s[i+len(p)-1])-ord('a')
            sa[left] -= 1; sa[right] += 1
            if sa == sp: res.append(i)
        return res

# @lc code=end

