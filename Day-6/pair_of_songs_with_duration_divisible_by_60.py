class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        count = 0
        d = {}
        for i in time:
            r = i % 60
            if (60 - r) in d:
                count += d[(60-r)]
            if r == 0 and r in d:
                count += d[r]
            if r in d:
                d[r] += 1
            else:
                d[r] = 1
        
        return count