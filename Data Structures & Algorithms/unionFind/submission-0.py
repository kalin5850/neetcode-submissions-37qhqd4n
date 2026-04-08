class UnionFind:
    
    def __init__(self, n: int):
        self.size = n
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        
        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.par[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.par[root_x] = root_y
            else:
                self.par[root_y] = root_x
                self.rank[root_x] += 1
            self.size -= 1

            return True

        return False

    def getNumComponents(self) -> int:
        return self.size

