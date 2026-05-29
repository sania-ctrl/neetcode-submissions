class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # starting time: 3:14
        flag = 0
        traversed = set()

        for i in range(len(nums)):
            traversed.add(nums[i])

            if len(traversed) != i+1:
                flag = 1 
                return True 
                break

        if flag == 0: 
            return False
