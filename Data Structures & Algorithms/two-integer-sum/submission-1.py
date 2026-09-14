class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in my_dict:
                other_index = my_dict.get(complement)
                arr = [index, other_index]
                return (sorted(arr))
            else:
                my_dict[number] = index