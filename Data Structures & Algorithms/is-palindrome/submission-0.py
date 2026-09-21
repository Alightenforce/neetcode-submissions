class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch for ch in s if ch.isalnum())
        left = 0
        right = len(cleaned) - 1
        while left < right:
            if cleaned[left].lower() == cleaned[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True