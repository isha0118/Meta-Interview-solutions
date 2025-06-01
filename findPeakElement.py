class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        return left
        # '''
        # 0 1 2 3 4 5 6
        # 1 2 1 3 5 6 4
        # left 5
        # right 5
        # mid 4
        # num[mid] 5
        # num[mid+1] 6