#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (58.63%)
# Likes:    197
# Dislikes: 0
# Total Accepted:    32.4K
# Total Submissions: 55.1K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 
# 示例:
# 
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# 说明：
# 
# 
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    # 用数组作为key，数组长度26，出现的字符位置置为1。这样不论顺序，只要字母一样的key就一样。
    # def groupAnagrams(self, strs: [str]) -> [[str]]:
    #     dict, base = {}, ord("a")
    #     for s in strs:
    #         key = [0]*26
    #         for c in s:
    #             key[ord(c) - base] += 1
    #         key = tuple(key)
    #         if key in dict:
    #             dict[key].append(s)
    #         else:
    #             dict[key] = [s]
    #     return dict.values()
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        def keyForStr(s: str) -> tuple:
            key, base = [0]*26, ord("a")
            for c in s: key[ord(c) - base] += 1
            return tuple(key)

        dic = defaultdict(list)
        for s in strs: dic[keyForStr(s)].append(s)
        return dic.values() 



# print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# @lc code=end

