class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a_index, a_value in enumerate(nums):
            for b_index, b_value in enumerate(nums):
                if a_index == b_index:
                    continue
                if a_value+b_value == target:
                    return [a_index, b_index]
