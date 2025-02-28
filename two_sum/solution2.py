""" Solution has time complexity of O(nlgn)"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = nums.copy()
        # O(nlgn) best case scenario for sorting
        nums_sorted.sort()
        
        # O(n)
        while True:
            nums_len = len(nums_sorted)
            
            min_index = 0
            max_index = nums_len-1
            min_el = nums_sorted[min_index]
            max_el = nums_sorted[max_index]

            if (min_el+max_el)==target:
                if min_el==max_el:
                    first_index = nums.index(min_el)
                    second_index = nums.index(max_el,first_index+1)
                else:
                    first_index = nums.index(min_el)
                    second_index = nums.index(max_el)
                return [first_index,second_index]

            elif (min_el+max_el)>target:
                nums_sorted = nums_sorted[min_index:max_index]
                continue
            elif (min_el+max_el)<target:
                nums_sorted = nums_sorted[min_index+1:max_index+1]
                continue
           
        return []