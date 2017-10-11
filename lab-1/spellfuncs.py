import re
import string


class SpellFuncs:
    def __init__(self, dictionary):
        self.dictionary = dictionary.read().splitlines()

    def clean_word(self, word):
        """
        Returns word without punctuations and numbers
        """
        if re.findall(r"[0-9]", word):
            pass
        word = word.lower()
        word = word.translate(str.maketrans('', '',
                                            string.punctuation))
        return(word)

    def create_dictonary(self, file):
        dictionary = file.read().splitlines()
        return(dictionary)

    def misspelled(self, file):
        """
        Returns a list of mispelled words in a file
        """
        mispelled = list()
        dictionary = self.dictionary
        for line in file:
            words = line.split()
            for word in words:
                word = self.clean_word(word)
                if word not in dictionary:
                    mispelled.append(word)
        return(mispelled)

    def suggestions(self, mispelled):
        """
        Given a list of mispelled words, returns a list of
        suggesstions for those words
        """
        suggestions = list()
        suggestions += self.insert_char(mispelled)
        suggestions += self.remove_char(mispelled)
        suggestions += self.switch_char(mispelled)
        return(suggestions)

    def insert_char(self, word):
        """
        Inserts a char in each index of a word, and returns a list of
        words where the insert is a correct word
        """
        dictionary = self.dictionary
        suggestions = list()
        for index, char in enumerate(word):
            for c in string.ascii_lowercase:
                temp = word
                if index == 0:
                    temp = (c + word)
                    if temp in dictionary:
                        suggestions.append(temp)
                elif index + 1 == len(word):
                    temp = (word + c)
                    if temp in dictionary:
                        suggestions.append(temp)
                else:
                    temp = (word[:index] + c + word[index + 1:])
                    if temp in dictionary:
                        suggestions.append(temp)
        return(suggestions)

    def remove_char(self, word):
        """
        Removes a char in each index of a word, and returns a list of words
        where removing a char produces a correct word
        """
        dictionary = self.dictionary
        suggestions = list()
        for index, char in enumerate(word):
            temp = (word[:index] + word[index + 1:])
            if temp in dictionary:
                suggestions.append(temp)
        return(suggestions)

    def switch_char(self, word):
        """
        Creates all possible permutations of characters in a word, and returns
        a list of words where the permutation is a correct word
        """
        dictionary = self.dictionary
        suggestions = list()
        for index, char in enumerate(word):
            if index == 0 or index == len(word) - 1:
                first_char = word[0]
                last_char = word[-1]
                temp = (last_char + word[1:-1] + first_char)
                if temp in dictionary:
                    suggestions.append(temp)
            else:
                temp = (word[:index] + word[index + 1] +
                        word[index] + word[index + 2:])
                if temp in dictionary:
                    suggestions.append(temp)
        return(suggestions)
