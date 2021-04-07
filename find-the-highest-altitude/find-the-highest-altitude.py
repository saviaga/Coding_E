class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest =0
        for elem in gain:
            altitude += elem
            if altitude > highest:
                highest = altitude
            
        return highest
        