class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     seen = {}
    #     for i, num in enumerate(nums):
    #         needed = target - num
    #         if needed in seen:
    #             return [seen[needed], i ]
    #         seen[num] = i 
    #     return
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range( len(nums)-1):
            for j in range( i+1, len(nums)):
                if nums[i] + nums[j] ==target:
                    return [i,j]
