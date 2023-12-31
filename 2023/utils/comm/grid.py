from copy import deepcopy
from typing import List

class Grid:
    def __init__(self, content: List[List]=None, sep: str=""):
        self.content = deepcopy(content) if content else []
        w = self.shape[1]
        for row in self.content:
            assert len(row) == w
        self.sep = sep
    def append_row(self, row: list):
        if self.content:
            assert len(row) == self.shape[1]
        self.content.append(deepcopy(row))

    def pad(self, fill_value="."):
        # pad two columns, then two rows
        for i, row in enumerate(self.content):
            self.content[i] = [(fill_value, i+1, 0)] + row + [(fill_value, i+1, len(row)+1)]
        first_row = [(fill_value, 0, j) for j in range(len(self.content[0]))]
        last_row = [(fill_value, len(self.content)+1, j) for j in range(len(self.content[0]))]
        self.content = [first_row] + self.content + [last_row]

    def __str__(self):
        rows_string = '\n'.join(
            self.sep.join(str(elem) for elem in line_list)
            for line_list in self.content
            )
        return rows_string

    def __getitem__(self, coords):
        i, j = coords
        return self.content[i][j]

    def __setitem__(self, coords, elem):
        i, j = coords
        self.content[i][j] = elem

    @property
    def shape(self):
        return len(self.content), len(self.content[0])

    def get_subset(self, i_min, i_max, j_min, j_max):
        subset = Grid([self.content[i][j_min: j_max+1] for i in range(i_min, i_max+1)])
        return subset
    