class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = []
        if numRows == 0:
            return ans
        
        else:
            row = []
            row.append(1)
            ans.append(row)
            
            for i in range(1, numRows):
                prev = ans[i-1]
                new = []
                
                new.append(1)
                
                j = 1
                for j in range(1, i):
                    new.append(prev[j-1] + prev[j])
                
                new.append(1)
                ans.append(new)
        
            return ans