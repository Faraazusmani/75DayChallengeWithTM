class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:              #create a dictionary to store frequency of each element
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for i in d:
            if d[i] > len(nums)//2:     #d[i] is the frequency of ith key in dictionary 
                return i