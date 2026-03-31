class TimeMap:

    def __init__(self):
        # hashmap to store list of values
        self.keyMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # checking if key 
        if key not in self.keyMap :
            self.keyMap[key] = []
        self.keyMap[key].append([timestamp, value])
    

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyMap:
            return ""

        values = self.keyMap[key]
        left, right = 0, len(values)-1
        ans = ''

        # ["alice", "happy", 1] ["alice", "happy", 5] ["alice", "happy", 7]
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                ans = values[mid][1]
                left = mid+1
            else:
                right = mid-1

        return ans
        
        
        
        
        
