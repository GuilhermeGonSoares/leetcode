class Solution(object):
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (start + end) // 2

            if nums[middle] == target:
                return middle
            
            if nums[middle] > target:
                end = middle - 1
            
            if nums[middle] < target:
                start = middle + 1
        return start

s = Solution()
print(s.searchInsert([2,5], 1))