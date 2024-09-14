import re

class Dictionary:
    def __init__(self, word_file):
        self.words = set()
        with open(word_file, 'r') as f:
            for word in f:
                self.words.add(word.strip().upper())

    def is_valid_word(self, word):
        return word.upper() in self.words


if __name__ == '__main__':
    # Example usage:
    dictionary = Dictionary('dictionary.csv')
    print(dictionary.is_valid_word('hello'))  # True if 'hello' is in the dictionary
