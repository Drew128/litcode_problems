class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        masks = [str(bin(i)).split('b')[1][::-1] for i in range(2**len(nums))]
        for mask in masks:
            new = sorted([num for num, bit in zip(nums, mask) if int(bit)])
            if new not in result: result.append(new)
        return result
