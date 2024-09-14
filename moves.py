import itertools
import operator
import string
from operator import itemgetter

from words import Dictionary


class ScrabbleMoveGenerator:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def generate_moves(self, rack, board):
        # Generate permutations of letters in the rack
        possible_words = []
        for length in range(1, len(rack) + 1):
            for perm in itertools.permutations(rack, length):
                word = ''.join(perm)
                if self.dictionary.is_valid_word(word):
                    possible_words.append(word)
        # TODO: Filter based on where the words can be placed on the board
        # TODO: Add combinations with letters of the board
        return possible_words


if __name__ == '__main__':
    move_generator = ScrabbleMoveGenerator(Dictionary('dictionary.csv'))


    alphabet = string.ascii_lowercase
    for letter in alphabet:
        moves = move_generator.generate_moves("lwgpyia" + letter, None)
        if not moves: continue
        words_with_length = [(len(word), word) for word in moves]
        best_length, _ = max(words_with_length)
        best_words = list(map(operator.itemgetter(1), filter(lambda x: x[0] == best_length, words_with_length)))
        print(f"{letter} : " + ", ".join(best_words))

