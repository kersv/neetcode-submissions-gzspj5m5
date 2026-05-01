class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # recursion

        maxHeap = [-s for s in stones]

        
        def rec(rocks):
            if len(rocks) <= 1:
                return abs(rocks[0]) if rocks else 0
            
            heapq.heapify(rocks)

            firstStone = heapq.heappop(rocks)
            secondStone = heapq.heappop(rocks)

            diff = firstStone - secondStone
            heapq.heappush(rocks, diff)

            return rec(rocks)

        return rec(maxHeap)


        


        

