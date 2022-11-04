class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            if start == end:
                break
            elif nums[middle] > target: #Então target tem que estar à esquerda
                end = middle - 1
            
            elif nums[middle] < target: #Então target tem que estar à direita
                start = middle + 1
        return -1
  
s = Solution()
print(s.search([-1,0,3,5,9,12], 1))