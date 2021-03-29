#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (39.92%)
# Likes:    192
# Dislikes: 0
# Total Accepted:    26.6K
# Total Submissions: 64.6K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
# 
# 示例: 
# 
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 
# 
# 进阶:
# 
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
# 
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: [int]) -> int:
        left = cur_sum = 0
        result = float('inf')
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= s:
                result = min(result, right - left + 1)
                cur_sum -= nums[left]
                left += 1
        return result if result != float('inf') else 0

# print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))
# print(Solution().minSubArrayLen(4, [1,4,4]))
# print(Solution().minSubArrayLen(5, [1,1,1,1,1,3,2]))    

# @lc code=end

