class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        highest_frequencies = []
        for number in nums:
            my_dict[number] = my_dict.get(number, 0) + 1
        sorted_dictionary_by_amount = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        tuples_sorted_by_amount = (list(sorted_dictionary_by_amount))
        for topK in range(k):
            highest_frequencies.append(tuples_sorted_by_amount[topK])
        return (highest_frequencies)