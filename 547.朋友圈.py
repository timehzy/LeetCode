#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#
# https://leetcode-cn.com/problems/friend-circles/description/
#
# algorithms
# Medium (52.27%)
# Likes:    148
# Dislikes: 0
# Total Accepted:    17.9K
# Total Submissions: 33.4K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C
# 的朋友。所谓的朋友圈，是指所有朋友的集合。
# 
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j
# 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
# 
# 示例 1:
# 
# 
# 输入: 
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# 输出: 2 
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
# 
# 
# 注意：
# 
# 
# N 在[1,200]的范围内。
# 对于所有学生，有M[i][i] = 1。
# 如果有M[i][j] = 1，则有M[j][i] = 1。
# 
# 
#

# @lc code=start
class Solution:
    # def findCircleNum(self, M: [[int]]) -> int:
    #     m = len(M)
    #     p = [i for i in range(m)]

    #     def parent(i):
    #         root = i
    #         while p[root] != root:
    #             root = p[root]
    #         while p[i] != i:
    #             t = i; i = p[i]; p[t] = root
    #         return root

    #     def union(i, j):
    #         ri = parent(i)
    #         rj = parent(j)
    #         p[rj] = ri

    #     for i in range(m):
    #         for j in range(i, m):
    #             if M[i][j] == 1:
    #                 union(i, j)

    #     return len(set([parent(i) for i in p]))

    class UnionSet:
            def __init__(self, n: int):
                self.count = n
                self.ids = [i for i in range(n)]
                self.sz = [1]*n
            
            def find(self, p):
                root = p
                while self.ids[root] != root: root = self.ids[root]
                while self.ids[p] != p:
                    temp = p; p = self.ids[p]; self.ids[temp] = root
                return root
                
            def union(self, p, q):
                rootp = self.find(p)
                rootq = self.find(q)
                if rootp == rootq: return
                if self.sz[rootp] < self.sz[rootq]:
                    self.ids[rootp] = rootq; self.sz[rootq] += self.sz[rootp]
                else:
                    self.ids[rootq] = rootp; self.sz[rootp] += self.sz[rootq]
                self.count -= 1

    def findCircleNum(self, M: [[int]]) -> int:
        if not M: return 0
        us = self.UnionSet(len(M))
        for i in range(len(M)):
            for j in range(i, len(M)):
                if M[i][j] == 1:
                    us.union(i, j)
        return us.count
            
    
    def trulyMostPopular(self, names: [str], synonyms: [str]) -> [str]:
        us = {}

        def find(name: str):
            root = name
            while us[root] != root: root = us[root]
            while us[name] != name:
                temp = name; name = us[name]; us[name] = temp
            return root
        
        def union(p, q):
            rootp = find(p)
            rootq = find(q)
            us[rootp] = rootq

        # 构建并查集
        for name in synonyms:
            nameArr = name.strip(["(", ")"]).split(",")
            for n in nameArr:
                
        



# @lc code=end

