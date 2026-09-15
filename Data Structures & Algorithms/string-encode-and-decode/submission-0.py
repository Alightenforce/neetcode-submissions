class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            word_length= len(word)
            string += str(word_length) + "#" + word
        return string

    def decode(self, s: str) -> List[str]:
        print (s)
        arr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            arr.append(s[i:j])
            i=j
        return arr