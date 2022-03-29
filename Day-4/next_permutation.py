class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if nums[::-1] == sorted(nums):
            nums.sort()
        
        
        # find the index till which the array is in an increasing order on reverse itereation of the array
        # [1,3,5,4,2]  index x = 1
        else:
            for i in range(len(nums)-1, -1, -1):
                if nums[i-1] < nums[i]:
                    x = i-1
                    break
            #print(x)
            # on reverse iteration find the index of the first element which is is greater than the element at index x
            # [1,3,5,4,2] index y = 3
            for i in range(len(nums)-1, -1, -1):
                if nums[i] > nums[x]:
                    y = i
                    break
            #print(y)
            # swap the two numbers at indices x and y
            # [1,4,5,3,2]

            nums[x], nums[y] = nums[y], nums[x]
            
            
            # [1,4] remains same and [5,3,2] is [2,3,5] (need not be sorted, just reversed)
            x += 1
            j = len(nums) - 1
            while x < j:
                nums[x], nums[j] = nums[j], nums[x]
                x += 1
                j -= 1