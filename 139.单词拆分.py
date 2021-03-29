#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (42.70%)
# Likes:    338
# Dislikes: 0
# Total Accepted:    37.8K
# Total Submissions: 86.6K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 
# 说明：
# 
# 
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 
# 
# 示例 2：
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 
#

# @lc code=start
class Solution:
    # def wordBreak(self, s: str, wordDict: [str]) -> bool:
    #     def search(target: str):
    #         if len(target) == 0:
    #             return True
    #         for word in wordDict:
    #             if word in target:
    #                 remains = target.split(word)
    #                 found = True
    #                 for r in remains:
    #                    if not search(r): 
    #                        found = False
    #                        break
    #                 if found: return True

    #         return False
    #     return search(s)
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]

print(Solution().wordBreak("leetcode", ["leet","code"]))
print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

# @lc code=end

