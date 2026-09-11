class Solution:
    def hammingWeight(self, n: int) -> int:
        if n > 0:
            ones = 1
        else: 
            ones = 0
            
        while n > 1:
            m = n % 2 
            ones = ones + m 
            n = int(n/2)
        return int(ones)