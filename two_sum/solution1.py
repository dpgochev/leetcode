"""" Solution has time complexity of O(n^2)"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            first_index=i
            for j in range(i+1,len(nums)):
                second_index=j
                if nums[first_index]+nums[second_index] == target:
                    return [first_index,second_index]