class UnionSet:
    def __init__(self, p):
        self.p = [i for i in range(p)]
    
    def parent(self, i):
        root = i
        while self.p[root] != root:
            root = self.p[root]

        while self.p[i] != i:
            x = i; i = self.p[i]; self.p[x] = root
        
        return root

    def union(self, i, j):
        pi = self.parent(i)
        pj = self.parent(j)
        self.p[pj] = pi
    
u = UnionSet(5)
print(u.p)#[0, 1, 2, 3, 4]
u.union(1, 2)
print(u.p)#[0, 2, 2, 3, 4]
u.union(2, 3)
print(u.p)#[0, 2, 3, 3, 4]
u.union(4,3)
print(u.p)#[0, 2, 3, 4, 4]