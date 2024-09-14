from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeAlias
    CellPos = tuple[int, int]
    rangeIndication = tuple[int, int] | tuple[int, int, int]
    rangeIndicationOptional = rangeIndication | None



EMPTY_CELL = ' '
tile_values = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
    'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, EMPTY_CELL: 0
}


class Cell:

    @staticmethod
    def gen_range(i_range: rangeIndication, j_range: rangeIndicationOptional = None) -> list[CellPos]:
        if j_range is None:
            j_range = i_range

        return [(i, j) for i in range(*i_range) for j in range(*j_range)]


    triple_word_cells: set[CellPos] = set((row, column) for column in range(0, 15, 7) for row in range(0, 15, 7))
    double_word_cells: set[CellPos] = set(
        gen_range((1, 5)) +
        gen_range((10, 15)) +
        gen_range((10, 15), (4, 0, -1)) +
        gen_range((1, 5), (14, 9, -1)) +
        [(7, 7)]
    )
    triple_letter_cells: set[CellPos] = {
        (5, 1), (9, 1),
        (1, 5), (5, 5), (9, 5), (13, 5),
        (1, 9), (5, 9), (9, 9), (13, 9),
        (5, 13), (9, 13),
    }
    double_letter_cells: set[CellPos] = {
        (3, 0), (11, 0),
        (6, 2), (8, 2),
        (0, 3), (7, 3), (14, 3),
        (2, 6), (6, 6), (8, 6), (12, 6),
        (3, 7), (11, 7),
        (2, 8), (6, 8), (8, 8), (12, 8),
        (0, 11), (7, 11), (14, 11),
        (6, 12), (8, 12),
        (3, 14), (11, 14),
    }

    @property
    def get_world_value(self):
        current = (self.row, self.column)
        return 1 + (current in Cell.double_word_cells) + (current in Cell.triple_word_cells) * 2

    @property
    def get_letter_value(self):
        current = (self.row, self.column)
        return 1 + (current in Cell.double_letter_cells) + (current in Cell.triple_letter_cells) * 2

    def __init__(self, row, column, letter=EMPTY_CELL):
        self.letter = letter
        self.row = row
        self.column = column


class ScrabbleBoard:
    def __init__(self):
        self.board = [[Cell(row, column) for column in range(15)] for row in range(15)]

    def display(self):
        for row in self.board:
            print(' '.join(cell if cell else '.' for cell in row))

