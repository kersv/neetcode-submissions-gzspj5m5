class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # recursion

        maxHeap = [-s for s in stones]

        heapq.heapify(maxHeap)
        
        def rec(rocks):
            if len(rocks) <= 1:
                return abs(rocks[0]) if rocks else 0
            

            firstStone = heapq.heappop(rocks)
            secondStone = heapq.heappop(rocks)

            diff = firstStone - secondStone
            if diff < 0:
                heapq.heappush(rocks, diff)

            return rec(rocks)

        return rec(maxHeap)


        


        

