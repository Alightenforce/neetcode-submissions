class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        fast = 0
        bigStr = ""
        longest = 0
        existing_char = set()

        while fast < len(s):
            if s[fast] not in existing_char:
                existing_char.add(s[fast])
                bigStr += s[fast]
            else:
                while s[fast] in existing_char:
                    existing_char.discard(s[slow])
                    slow += 1
                    bigStr = bigStr[1:]
                existing_char.add(s[fast])
                bigStr += s[fast]
            fast += 1
            longest = max(longest, len(bigStr))
        return longest

