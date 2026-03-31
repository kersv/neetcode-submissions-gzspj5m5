class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # low, high = lowest speed (1 banana per hour), highest speed(max banana in a pile)
        high = 0
        low = 1
        for banana in piles:
            high = max(high, banana)
        
        minSpeed = high
        # find the middle = speed between the speeds(low and high)
        while low <= high:
            middle = (low + high) // 2 
            totalHour = 0

            for banana in piles:
                totalHour += math.ceil(banana / middle)
                
            print(totalHour)
            if totalHour > h:
                low = middle +1
            else:
                minSpeed = min(minSpeed, middle)
                high = middle -1

        return minSpeed

        # calc if it the speed could finish all the bananas in h hour