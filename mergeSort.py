from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]
        left_sorted = self.sortArray(left_half)
        right_sorted = self.sortArray(right_half)
        return self.merge(left_sorted, right_sorted)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        left_index = 0
        right_index = 0
        
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        
        # append the remaining
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        
        return result


solution = Solution()
sortednum = solution.sortArray([4, 100, 20, 50, 1, 20])
print(sortednum)
