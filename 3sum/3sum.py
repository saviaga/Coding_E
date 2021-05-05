class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        
        def search_pair(arr, target_sum, left, triplets):
            right = len(arr) - 1
            while(left < right):
                current_sum = arr[left] + arr[right]
                if current_sum == target_sum:  # found the triplet
                    new_triplet =[-target_sum, arr[left], arr[right]] 
                    if new_triplet not in triplets:
                        triplets.append(new_triplet)
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1  # skip same element to avoid duplicate triplets
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1  # skip same element to avoid duplicate triplets
                elif target_sum > current_sum:
                    left += 1  # we need a pair with a bigger sum
                else:
                    right -= 1  # we need a pair with a smaller sum

            
        #We sort the array
        arr.sort()
        triplets = []
        for i in range(len(arr)):
            search_pair(arr, -arr[i], i+1, triplets)
        return triplets
            

        