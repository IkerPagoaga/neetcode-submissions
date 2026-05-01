class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        
        is_duplicate = False

        for num in nums:
            if nums.count(num) > 1:
                is_duplicate = True
                break
            else:
                is_duplicate = False
        
        return is_duplicate