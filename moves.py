import sys
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


def filter_longest_words(moves):
    if not moves: return []
    words_with_length = [(len(word), word) for word in moves]
    best_length, _ = max(words_with_length)
    best_words = list(map(operator.itemgetter(1), filter(lambda x: x[0] == best_length, words_with_length)))
    return best_words


if __name__ == '__main__':
    if len(sys.argv) > 1:
        rack = sys.argv[1]
    else:
        rack = input("enter rack : ")

    move_generator = ScrabbleMoveGenerator(Dictionary('dictionary.csv'))
    default = set(move_generator.generate_moves(rack, None))
    print("Default words :", *default)
    all_words = set()
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        moves = move_generator.generate_moves(rack + letter, None)
        moves = list(set(moves) - default)
        # best_words = filter_longest_words(moves)
        best_words = moves

        all_words.update(best_words)
        print(f"{letter} : " + ", ".join(best_words))

    best_of_all = filter_longest_words(all_words)
    print("BEST OF ALL : ")
    print(*best_of_all)
    print("Total words amount :", len(all_words))
