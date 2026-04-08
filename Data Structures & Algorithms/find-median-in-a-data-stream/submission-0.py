import heapq

class MedianFinder:

    def __init__(self):
        self.smaller = [] # max-heap
        self.larger = [] # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smaller, -1 * num)
        if self.smaller and self.larger and (-1 * self.smaller[0]) > self.larger[0]:
            value = -1 * heapq.heappop(self.smaller)
            heapq.heappush(self.larger, value)
        
        if len(self.smaller) - len(self.larger) > 1:
            value = -1 * heapq.heappop(self.smaller)
            heapq.heappush(self.larger, value)
        elif len(self.larger) - len(self.smaller) > 1:
            value = heapq.heappop(self.larger)
            heapq.heappush(self.smaller, -1 * value)
        

    def findMedian(self) -> float:
        if len(self.smaller) > len(self.larger):
            return -1 * self.smaller[0]
        elif len(self.smaller) < len(self.larger):
            return self.larger[0]
        
        return (-1 * self.smaller[0] + self.larger[0]) / 2
        
        