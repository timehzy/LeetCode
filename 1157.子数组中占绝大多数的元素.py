#
# @lc app=leetcode.cn id=1157 lang=python3
#
# [1157] 子数组中占绝大多数的元素
#
# https://leetcode-cn.com/problems/online-majority-element-in-subarray/description/
#
# algorithms
# Hard (20.15%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    1.2K
# Total Submissions: 4.7K
# Testcase Example:  '["MajorityChecker","query","query","query"]\n[[[1,1,2,2,1,1]],[0,5,4],[0,3,3],[2,3,2]]'
#
# 实现一个 MajorityChecker 的类，它应该具有下述几个 API：
# 
# 
# MajorityChecker(int[] arr) 会用给定的数组 arr 来构造一个 MajorityChecker 的实例。
# int query(int left, int right, int threshold) 有这么几个参数：
# 
# 0 <= left <= right < arr.length 表示数组 arr 的子数组的长度。
# 2 * threshold > right - left + 1，也就是说阈值 threshold 始终比子序列长度的一半还要大。
# 
# 
# 
# 
# 每次查询 query(...) 会返回在 arr[left], arr[left+1], ..., arr[right] 中至少出现阈值次数
# threshold 的元素，如果不存在这样的元素，就返回 -1。
# 
# 
# 
# 示例：
# 
# MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
# majorityChecker.query(0,5,4); // 返回 1
# majorityChecker.query(0,3,3); // 返回 -1
# majorityChecker.query(2,3,2); // 返回 2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 20000
# 1 <= arr[i] <= 20000
# 对于每次查询，0 <= left <= right < len(arr)
# 对于每次查询，2 * threshold > right - left + 1
# 查询次数最多为 10000
# 
# 
#

# @lc code=start
class MajorityChecker:

    def __init__(self, arr: List[int]):
        

    def query(self, left: int, right: int, threshold: int) -> int:
        


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
# @lc code=end

