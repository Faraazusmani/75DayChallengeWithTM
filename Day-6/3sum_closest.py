class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        #print(nums)
        
        # store all 3 sums
        z = [] 
        for i in range(len(nums)):
            x = i+1
            y = len(nums) - 1
            while x < y:
                if nums[i] + nums[x] + nums[y] == target:
                    return target
                elif nums[i] + nums[x] + nums[y] < target:
                    z.append(nums[i] + nums[x] + nums[y])
                    x += 1
                else:
                    z.append(nums[i] + nums[x] + nums[y])
                    y -= 1
        #print(z)

        z.append(target)
        z.sort()
        #print(z)
        if target == z[0]:
            return z[1]
        elif target == z[-1]:
            return z[len(z)-2]
        else:
            idx = z.index(target)
            p = abs(target - z[idx - 1])
            #print(p)
            q = abs(z[idx + 1] - target)
            #print(q)
            if p < q:
                return z[idx - 1]
            else:
                return z[idx + 1]