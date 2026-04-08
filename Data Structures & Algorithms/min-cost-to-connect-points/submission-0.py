import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # build adjacency list
        adj = {}
        for i in range(len(points)):
            adj[i] = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([j, d])
                adj[j].append([i, d])
        
        minheap = []
        min_cost = 0
        visit = set()
        visit.add(0)

        for neighbor, weight in adj[0]:
            heapq.heappush(minheap, [weight, 0, neighbor])

        while minheap:
            weight, n1, n2 = heapq.heappop(minheap)
            if n2 in visit:
                continue
            visit.add(n2)
            min_cost += weight
            for neighbor, weight in adj[n2]:
                if neighbor not in visit:
                    heapq.heappush(minheap, [weight, n2, neighbor])

        return min_cost
