class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        j = 0
        while j < n:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        j = i
        while j < n:
            if nums[j] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1