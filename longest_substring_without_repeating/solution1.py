# O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest_non_repeating_sub = s[0]
        current_non_repeating_sub = s[0]
        start_index = 0
        length = 1
        current_length = 1
        dic = {s[0]: True}
        i = 1
        while i < (len(s)):
            if dic.get(s[i], False):
                current_length = 0
                current_non_repeating_sub = ""
                i = start_index + 1
                start_index = i
                dic = {}
            else:
                dic[s[i]] = True
                current_length += 1
                current_non_repeating_sub += s[i]
                i += 1
            if len(current_non_repeating_sub) > len(longest_non_repeating_sub):
                longest_non_repeating_sub = current_non_repeating_sub
                length = current_length

        return length
