#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (37.66%)
# Likes:    236
# Dislikes: 0
# Total Accepted:    44.7K
# Total Submissions: 113.9K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
# 
# 
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 
# 
# 示例:
# 
# 现有矩阵 matrix 如下：
# 
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
# 
# 
# 给定 target = 5，返回 true。
# 
# 给定 target = 20，返回 false。
# 
#

# @lc code=start

import math
class Solution:
    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     if not matrix or not matrix[0]: return False
    #     # 规律是：取矩阵对中间点，若目标元素小于中间点，则一定位于右下方以外的区域，若大于中间点则位于左上方以外的区域。分别对相应区域继续搜索即可。
    #     # 该方法速度不理想，仅仅击败10%的人
    #     def helfSearch(top_left: (int, int), bottom_right: (int, int)):
    #         top, left = top_left
    #         bottom, right = bottom_right
    #         if left > right or top > bottom: return False
    #         mid = (int((top + (bottom-top)/2)), int((left+(right-left)/2)))
    #         mid_val = matrix[mid[0]][mid[1]]
    #         if target == mid_val:
    #             return True
    #         if top_left == bottom_right:
    #             return False

    #         if target < mid_val:
    #             return helfSearch(top_left, (bottom, mid[1]-1)) or helfSearch((top, mid[1]), (mid[0]-1,right))
    #         else:
    #             return helfSearch((mid[0]+1, left), (bottom, mid[1])) or helfSearch((top, mid[1]+1), bottom_right)

    #     return helfSearch((0, 0), (len(matrix)-1, len(matrix[0])-1))
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        width = len(matrix[0])
        col, row = 0, len(matrix)-1
        while col < width and row >= 0:
            if target > matrix[row][col]:
                col += 1
            elif target < matrix[row][col]:
                row -= 1
            else:
                return True
        return False
        
print(Solution().searchMatrix( [[1,2,3,4,5],
                                [6,7,8,9,10],
                                [11,12,13,14,15],
                                [16,17,18,19,20],
                                [21,22,23,24,25]], 5))

print(Solution().searchMatrix( [[1,4,7,11,15],
                                [2,5,8,12,19],
                                [3,6,9,16,22],
                                [10, 13, 14, 17, 24],
                                [18, 21, 23, 26, 30]], 5))
print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]], 20))

print(Solution().searchMatrix( [[5 , 6,10,14],
                                [6 ,10,13,18],
                                [10,13,18,19]], 14))

# @lc code=end