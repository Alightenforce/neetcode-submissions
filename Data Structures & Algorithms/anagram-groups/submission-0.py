class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        answer_list=[]
        for word in strs:
            sorted_word = "".join(sorted(word))
            my_dict.setdefault(sorted_word, []).append(word)
        for word, anagrams in my_dict.items():
            answer_list.append(anagrams)
        return answer_list


