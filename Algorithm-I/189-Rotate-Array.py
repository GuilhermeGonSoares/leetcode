class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p = - (k % len(nums))
        if len(nums[:p]):
            nums[:p], nums[p:] = nums[p:], nums[:p]
        else:
            nums[p:], nums[:p] = nums[:p], nums[p:]


        

s = Solution()
s.rotate([1,2,3,4,5,6,7], 7)