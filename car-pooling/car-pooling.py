class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        
        list_times_cap = []
        
        for cap,start,end in trips:
            list_times_cap.append((start,cap))
            list_times_cap.append((end,-cap))
            
        list_times_cap.sort(key=lambda x:(x[0],x[1]))
       
        for start,cap in list_times_cap:
            
            capacity -=cap
            if capacity < 0:
                return False
        return True
            
        
            
        