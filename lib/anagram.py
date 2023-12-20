# your code goes here!
# define a class called anagram, then __initial__ two items, 
# 1. a given word, and a list of anagrams
# if the given word matches one of the words in the list as an anagram
# then return a list with all the matching anagrams
# otherwise, return an empty list
# make a sorted list with all the characters in the given word &
# the words in the list
# if a word in the list has all the same letters, it's an anagram

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = []
        for candidate in words:
            if candidate != self.word:
                if sorted(candidate) == sorted(self.word):
                    anagrams.append(candidate)
        return anagrams