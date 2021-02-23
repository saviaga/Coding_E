class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_elems = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict_elems[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        
        A = self.dict_elems[key]
        if A is None: return ""
       
        i = bisect.bisect(A,(timestamp, chr(127)))
        if i:
            return A[i-1][1] 
        else:
            return ""
                         
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)