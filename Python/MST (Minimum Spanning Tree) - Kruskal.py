class UnionFind(object):
    def __init__(self, n):
        self.f = [i for i in range(n)]
    def find(self,x):
        if x != self.f[x]:
            self.f[x] = self.find(self.f[x])
        return self.f[x]
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.f[x] = y
        
class Solution(object):
    def minCostToSupplyWater(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # MST (Minimum Spanning Tree)
        # kruskal
        UF = UnionFind(n)
        edges.sort(key=lambda edge: edge[2])
        res = 0
        for edge in edges:
            x = UF.find(edge[0])
            y = UF.find(edge[1])
            if x != y:
                res += edge[2]
                UF.union(x,y)
        return res

#test
n = 4
edges = [[0,1,1],[0,2,2],[0,3,2],[1,2,1],[2,3,1]]
ans = Solution().minCostToSupplyWater(n, edges)
print ans        
        