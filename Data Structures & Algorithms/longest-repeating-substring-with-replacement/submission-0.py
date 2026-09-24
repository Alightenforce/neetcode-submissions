class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slow = 0
        fast = 0
        my_dict = {}
        maxf = 0
        res = 0
        while fast < len(s):
            my_dict[s[fast]] = my_dict.get(s[fast], 0) + 1
            maxf = max(maxf, my_dict[s[fast]])
            while (fast - slow + 1) - maxf > k:
                my_dict[s[slow]] -= 1
                slow += 1
            res = max(res, fast - slow + 1)
            fast += 1
        return res

