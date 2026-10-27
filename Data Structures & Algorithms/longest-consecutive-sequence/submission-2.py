class UnionFind:
    def __init__(self,elements):
        self.parents={element:element for element in elements}
        self.size = {element: 1 for element in elements}
        self.max_size = 1 if elements else 0
        
    def find(self,x):
        if self.parents[x]!=x:
            self.parents[x]=self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parents[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            
            self.max_size = max(self.max_size, self.size[rootX])


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        unique_nums = set(nums)
        
        uf = UnionFind(unique_nums)
        
        for num in unique_nums:
            if num + 1 in unique_nums:
                uf.union(num, num + 1)
                
        return uf.max_size