class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """ brute force """
        # distance = []
        # result = []
        # for (x, y) in points:
        #     distance.append([(x ** 2 + y ** 2), (x, y)])
        # distance.sort()
        # for i in range(k):
        #     result.append(distance[i][1])

        # return result

        """ min heap """
        min_heap = []
        result = []
        for (x, y) in points:
            heapq.heappush(min_heap, [(x ** 2 + y ** 2), (x, y)])
        for _ in range(k):
            result.append(heapq.heappop(min_heap)[1])

        return result
