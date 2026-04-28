class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # heapq
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        print(maxHeap)

        # keep running until len of stones is 1
        # get two heaviest, and pop the smallest of the 2 or both if equal, and push the new weight of heaviest
        while len(maxHeap) > 1:
            firstStone = heapq.heappop(maxHeap)
            secondStone = heapq.heappop(maxHeap)

           
            newStone = firstStone - secondStone
            heapq.heappush(maxHeap, newStone)
        
        # return the weight of the stone
        return abs(maxHeap[0]) if maxHeap else 0

