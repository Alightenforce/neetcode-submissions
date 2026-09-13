class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            s_dict.setdefault(letter, 1)
        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            t_dict.setdefault(letter, 1)

        print (s_dict)
        print (t_dict)
        s_len = len(s)
        t_len = len(t)

        if s_len > t_len:
            main_dict = s_dict
            minor_dict = t_dict
        else:
            main_dict = t_dict
            minor_dict = s_dict

        for letter, amount in main_dict.items():
            amount_value = minor_dict.get(letter)
            if amount_value == amount:
                continue
            else:
                return False
        return True