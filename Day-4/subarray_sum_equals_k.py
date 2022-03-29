# approach 1
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i, j, ans = 0, 1, 0
        while j < len(nums):
            if sum(nums[i:j+1]) == k:
                ans += 1
                i = j
                j += 1
            elif sum(nums[i:j+1]) < k:
                j += 1
            else:
                i += 1
        return ans

# approach 2
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c_sum = 0
        result = 0
        
        d = { 0 : 1 }  # a map where subarray sum = 0 already occurs once
        for n in nums:
            c_sum += n
            diff = c_sum - k
            
            result += d.get(diff, 0)
            d[c_sum] = 1 + d.get(c_sum, 0)
        
        return result