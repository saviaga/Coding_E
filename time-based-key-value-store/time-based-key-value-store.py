class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_elems = collections.defaultdict(list)
    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict_elems[key].append((timestamp,value))
    
    '''[,,"get","get","set","get","get"]
        [,,["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
        
        dict_elems = {["foo","bar",1]
                      ["foo","bar2",4]}
'''
    def get(self, key: str, timestamp: int) -> str:
        
        items = self.dict_elems[key]

        left = 0
        right = len(items)
        while left < right:
            mid =  left + (right - left)//2
            if items[mid][0] > timestamp:
                right = mid
            else:
                left = mid+1         
        if left == 0:
            return ""
        return items[left-1][1] 
                         
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)