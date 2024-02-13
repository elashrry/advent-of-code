from typing import List, Tuple
from functools import reduce
from itertools import combinations

from aocutils import Parser


class Universe:
    def __init__(self, init_grid: List[List[str]], galaxy_loc_list: List[Tuple[int]]):
        self.init_grid = [row.copy() for row in init_grid]
        self.galaxy_loc_list = galaxy_loc_list.copy()

    def get_distance(self, loc1: Tuple[int], loc2: Tuple[int]):
        return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

    def expand(self, multiplier: int):
        # expand rows from last to first
        universe_width = len(self.init_grid)
        for i, row in enumerate(self.init_grid[-1::-1]):
            if "#" not in row:
                row_idx = universe_width - i - 1
                self.galaxy_loc_list = [
                    (g_i + multiplier - 1, g_j) if g_i > row_idx else (g_i, g_j)
                    for g_i, g_j in self.galaxy_loc_list
                ]
        # expand columns from last to first
        column_list = self._copy_transpose()
        universe_tr_width = len(column_list)
        for j, column in enumerate(column_list[-1::-1]):
            if "#" not in column:
                column_idx = universe_tr_width - j - 1
                self.galaxy_loc_list = [
                    (g_i, g_j + multiplier - 1) if g_j > column_idx else (g_i, g_j)
                    for g_i, g_j in self.galaxy_loc_list
                ]

    def _copy_transpose(self):
        return [
            [self.init_grid[i][j] for i in range(len(self.init_grid))]
            for j in range(len(self.init_grid[0]))
        ]


def parse_input(file_name: str):
    lines = Parser(file_name).get_lines()
    grid = []
    galaxy_loc_list = []
    i = 0
    for line in lines:
        line_list = []
        j = 0
        for ch in line:
            line_list.append(ch)
            if ch == "#":
                galaxy_loc_list.append((i, j))
            j += 1
        i += 1
        grid.append(line_list)
    return grid, galaxy_loc_list


def main():
    grid, galaxy_loc_list = parse_input("../AoC-input/2023/day11.txt")

    # part 1 and 2
    for i, mul in zip([1, 2], [2, 1e6]):
        universe = Universe(grid, galaxy_loc_list)
        universe.expand(mul)
        pairwise_distances = [
            universe.get_distance(loc1, loc2)
            for loc1, loc2 in combinations(universe.galaxy_loc_list, r=2)
        ]
        total = reduce(lambda x, y: x + y, pairwise_distances)
        print(f"part {i}: {total :.0f}")


if __name__ == "__main__":
    main()
