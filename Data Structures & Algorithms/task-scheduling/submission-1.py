class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # hashmap for counter
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]

        # heapq 
        heapq.heapify(maxHeap)
        print(maxHeap)

        # queue for wait time
        queue = deque()

        # return time at end to see time to complete all task
        time = 0


        while maxHeap or queue:
            time +=1
            # while the queue has values, pop them while it matches the time

            if maxHeap:
                val = heapq.heappop(maxHeap) +1
                if val != 0:
                    queue.append((val, time+n))

            while queue and queue[0][1] == time:
                val, time = queue.popleft()
                heapq.heappush(maxHeap, val)
            
        return time
            
            
        

