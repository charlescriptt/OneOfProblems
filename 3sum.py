class Solution:
    # == 0
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []       
        for i in range(len(nums)-2):
            left = i
            
            for j in range(i + 1, len(nums)-1):
                mid = j
                right = mid + 1
                for z in range(j + 1, len(nums)):
                    right = z
                    if(nums[left] + nums[right] + nums[mid] == 0):
                        out.append([nums[left], nums[mid], nums[right]])
        return out