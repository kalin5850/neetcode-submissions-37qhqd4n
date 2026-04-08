class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        result = []
        for (x, y) in points:
            distance.append([(x ** 2 + y ** 2), (x, y)])
        distance.sort()
        for i in range(k):
            result.append(distance[i][1])

        return result