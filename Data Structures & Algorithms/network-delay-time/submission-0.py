import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # define adjancency list
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        for s, d, w in times:
            adj[s].append([d, w])
        
        minheap = [[0, k]]
        shortest = {}
        t_min = -1

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            t_min = max(w1, t_min)
            
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap, [w1 + w2, n2])
        
        return t_min if len(shortest) == n else -1
