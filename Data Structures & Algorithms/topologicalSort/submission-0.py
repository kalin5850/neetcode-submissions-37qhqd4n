from collections import defaultdict, deque

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
        
        top_sort = []
        count = 0
        q = deque([i for i in range(n) if in_degree[i] == 0])

        while q:
            node = q.popleft()
            top_sort.append(node)
            count += 1
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        return top_sort if count == n else []