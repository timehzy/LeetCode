#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (42.62%)
# Likes:    152
# Dislikes: 0
# Total Accepted:    17.1K
# Total Submissions: 40K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
# 
# 返回滑动窗口中的最大值。
# 
# 
# 
# 示例:
# 
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
# ⁠ 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# 
# 提示：
# 
# 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
# 
# 
# 
# 进阶：
# 
# 你能在线性时间复杂度内解决此题吗？
# 
#

# @lc code=start
from collections import deque
class Solution:
    # def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
    #     if len(nums) * k == 0: return []
    #     if k == 1: return nums
    #     deq, res = deque(), [nums[0]]
    #     def clea_deq_forindex(i: int):
    #         if deq and deq[0] == i - k:
    #             deq.popleft()
    #         while deq and nums[i] > nums[deq[-1]]:
    #             deq.pop()
            
    #     for i in range(1, k):
    #         clea_deq_forindex(i)
    #         deq.append(i)
    #         if nums[i] > res[0]: res[0] = nums[i]

    #     for i in range(k, len(nums)):
    #         clea_deq_forindex(i)
    #         deq.append(i)
    #         res.append(nums[deq[0]])
        
    #     return res

    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        deq, res = deque(), []

        def clean_deq_index(i: int):
            if deq and deq[0] < nums[i]:
                deq.popleft()
            while deq and 

        for i in range(k):


print(Solution().maxSlidingWindow([1,3,1,2,0,5], 3))
# @lc code=end

