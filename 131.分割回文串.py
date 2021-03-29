#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (64.01%)
# Likes:    225
# Dislikes: 0
# Total Accepted:    23.7K
# Total Submissions: 36K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回 s 所有可能的分割方案。
# 
# 示例:
# 
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> [[str]]:
        # dfs搜索，若当前截取的不是回文串就剪枝
        res, path = [], []

        def dfs(start):
            if start == len(s):
                res.append(path.copy())
                return

            for i in range(start, len(s)):
                if not isPalindrome(start, i): continue
                path.append(s[start:i+1])
                dfs(i+1)
                path.pop(-1)

        def isPalindrome(start, end):
            while start < end:
                if s[start] != s[end]: 
                    return False
                start += 1; end -= 1
            return True
                   
        dfs(0)
        return res

# @lc code=end

