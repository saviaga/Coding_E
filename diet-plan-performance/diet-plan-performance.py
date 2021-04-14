class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        points = 0
        window_sum = 0
        start = 0
        for end in range(len(calories)):
            window_sum += calories[end]
            if end >= k-1:
                if window_sum < lower:
                    points-=1
                if window_sum > upper:
                    points+=1
                window_sum-=calories[start]
                start+=1
                    
        return points
            
        