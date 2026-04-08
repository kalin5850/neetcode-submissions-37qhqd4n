import heapq


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:        
        # build adjacency list
        adj = {}
        for i in range(n):
            adj[i] = []
        for n1, n2, w in edges:
            adj[n1].append([n2, w])
            adj[n2].append([n1, w])
        
        minheap = []
        count_weight = 0
        visted = set()
        visted.add(0)

        for neighbor, weight in adj[0]:
            heapq.heappush(minheap, [weight, 0, neighbor])

        while len(visted) < n:
            if not minheap:
                return -1
            weight, n1, n2 = heapq.heappop(minheap)
            if n2 in visted:
                continue
            count_weight += weight
            visted.add(n2)
            for neighbor, weight in adj[n2]:
                if neighbor not in visted:
                    heapq.heappush(minheap, [weight, n2, neighbor])
        
        return count_weight