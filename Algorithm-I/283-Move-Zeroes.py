class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        marca_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[marca_zero], nums[i] = nums[i], nums[marca_zero]
                marca_zero += 1

s = Solution()
print(s.moveZeroes([1,2,3,0,4]))