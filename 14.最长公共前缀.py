#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.94%)
# Likes:    783
# Dislikes: 0
# Total Accepted:    154.2K
# Total Submissions: 435.4K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        minLen = float('inf')
        print(minLen)
        for s in strs:
            if len(s) < minLen: minLen = len(s)
        
        for i in range(len(minLen)):
            
            for s in strs:

            
            
Solution().longestCommonPrefix(["flower","flow","flight"])   
# @lc code=end

