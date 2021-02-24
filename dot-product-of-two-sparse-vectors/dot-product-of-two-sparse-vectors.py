class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i in range(len(nums)):
            if nums[i]!=0:
                self.nonzeros[i]=nums[i]
        
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        prod = 0
        for idx,val in self.nonzeros.items():
            if idx in vec.nonzeros:
                prod+=val*vec.nonzeros[idx]
        
                
        return prod
            
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)