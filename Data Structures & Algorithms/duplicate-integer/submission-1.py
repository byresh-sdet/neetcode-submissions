class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = list()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.append(i)
        return False

        