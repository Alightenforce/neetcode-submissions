class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_list = sorted(nums)
        numbers = []
        for i in range(len(sorted_list)):
            current_value = sorted_list[i]
            left = i + 1
            right = len(sorted_list) - 1
            while left < right:
                my_sum = current_value + sorted_list[left] + sorted_list[right]
                if my_sum > 0:
                    right -= 1
                elif my_sum < 0:
                    left += 1
                else:
                    numbers.append([current_value, sorted_list[left], sorted_list[right]])
                    left += 1
                    right -= 1
        unique_triplets = [list(t) for t in set(tuple(x) for x in numbers)]
        return unique_triplets
            
