class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        
        def search_pair(arr, target_sum, start, triplets):
            end = len(arr) - 1
            
            while(start < end):
                current_sum = arr[start] + arr[end]
                if current_sum == target_sum:  # found the triplet
                    new_triplet =[-target_sum, arr[start], arr[end]] 
                    if new_triplet not in triplets:
                        triplets.append(new_triplet)
                    start += 1
                    end -= 1
                    while start < end and arr[start] == arr[start - 1]:
                        start += 1  # skip same element to avoid duplicate triplets
                    while start < end and arr[end] == arr[end + 1]:
                        end -= 1  # skip same element to avoid duplicate triplets
                elif target_sum > current_sum:
                    start += 1  # we need a pair with a bigger sum
                else:
                    end -= 1  # we need a pair with a smaller sum

            
        #We sort the array
        arr.sort()
        triplets = []
        for i in range(len(arr)):
            #y+z = -x
            #grab first element x (arr[i]), then try to fidn the next two: y + z
            search_pair(arr, -arr[i], i+1, triplets)
            
        return triplets
            

        