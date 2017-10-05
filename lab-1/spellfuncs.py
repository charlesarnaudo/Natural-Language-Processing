import re
import string


#def suggestion(word):
class SpellFuncs:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def spellcheck(self, word):
        if re.findall(r"[0-9]", word):
            pass
        word = word.lower()
        word = word.translate(str.maketrans('', '',
                                            string.punctuation))
        return(word)

    def suggestions(self, mispelled):
        suggestions = list()
        for word in mispelled:
            suggestions += self.insert_char(word)
        return(suggestions)


    def insert_char(self, word):
        """
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


    def remove_char(word, index):
        """
        """
        suggestions = list()
        for index, char in enumerate(word):
            return(word[:index] + word[index + 1:])


    def switch_char(word, index):
        """
        """
        if index == 0 or index == len(word) - 1:
            first_char = word[0]
            last_char = word[-1]
            return(last_char + word[1:-1] + first_char)
        else:
            return(word[:index] + word[index + 1] + word[index] + word[index + 2:])
