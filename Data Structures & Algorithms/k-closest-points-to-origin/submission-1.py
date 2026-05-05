class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []
        heapq.heapify(maxHeap)

        for val in points:
            x, y = val
            distance = pow(x,2)+pow(y,2)
            heapq.heappush(maxHeap, (distance*-1, val))
        

        
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

        ans = []
        for point in maxHeap:
            dist, pair = point
            ans.append(pair)
        
        return ans
    