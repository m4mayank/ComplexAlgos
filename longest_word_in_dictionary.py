#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

# If there is no answer, return the empty string.
# Example 1:
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

class Solution:    
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        dicti = {}
        ideal = ""
        lenth = 0
        for w in words:
            if len(w) == 1:
                dicti[w] = 1
                if len(w) > lenth:
                    lenth = len(w)
                    ideal = w
            else:
                if w[0:len(w)-1] in dicti:
                    dicti[w] = 1
                    if len(w) > lenth:
                        lenth = len(w)
                        ideal = w
        return ideal