class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        i, j = 0, len(height) - 1
        while i < j:
            if (j - i) * min(height[i], height[j]) > area:
                area = (j - i) * min(height[i], height[j])
            if height[i] <= height[j]:
                i += 1
            elif height[i] >= height[j]:
                j -= 1
        return area