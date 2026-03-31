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

        while left <= right:
            if values[right][0] <= timestamp:
                return values[right][1]
            else:
                right -= 1

        return ans
        
        
        
        
        
