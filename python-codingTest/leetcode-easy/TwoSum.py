class Solution:
    def twoSum(self, nums=[], target):
        firstIndex=0                    
        for i in nums:
            secondIndex=0
            for j in nums:
                if i+j == target:
                    if firstIndex != secondIndex:
                        return [firstIndex, secondIndex]
                secondIndex+=1
            firstIndex+=1