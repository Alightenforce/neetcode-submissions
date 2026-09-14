class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        size = len(nums)
        final_array = []
        bucket = [[] for _ in range(size + 1)]
        for number in nums:
            my_dict[number] = my_dict.get(number, 0) + 1
        for number, amount in my_dict.items():
            bucket[amount].append(number)
        for numbers in range(size,0,-1):
            for number in bucket[numbers]:
                final_array.append(number)
                if len(final_array) == k:
                    return final_array
