class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False

        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = s_dict.get(letter, 0) + 1
        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = t_dict.get(letter, 0) + 1

        for letter, amount in s_dict.items():
            amount_value = t_dict.get(letter)
            if amount_value == amount:
                continue
            else:
                return False
        return True