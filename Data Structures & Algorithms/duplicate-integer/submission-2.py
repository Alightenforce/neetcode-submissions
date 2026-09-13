class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        amount_max = []
        if len(nums) == 0:
            return False
        for number in nums:
            if number in my_dict:
                my_dict[number] += 1
            my_dict.setdefault(number, 1)
        # print (my_dict)
        for number, amount in my_dict.items():
            amount_max.append(amount)
        max_amount = max(amount_max)
        if max_amount == 1:
            return False
        else:
            return True
        