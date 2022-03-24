class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        c = 0
        if len(nums)>0:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j] == target:
                        c = 1
                        break
                if c!=0:
                    break
                
            return [i,j]
        
        else:
            return [0]