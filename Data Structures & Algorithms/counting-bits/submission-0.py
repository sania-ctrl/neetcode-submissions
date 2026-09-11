def f(i:int) -> int:
    if i == 0:
        return 0
    if i == 1: 
        return 1
    return f(i//2) + (i % 2)

class Solution:
    def countBits(self, n: int) -> List[int]:
        results = []
        for i in range(0, n+1):
            results.append(f(i))
        return results