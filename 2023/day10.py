from aocutils import Parser, Grid, timeit
from utils.day10 import Pipe, find_loop, infer_start_pipe_type, scan


def parse_input(file_name: str):
    lines = Parser(file_name).get_lines()
    grid = Grid()
    # elem location is i+1, j+1 because of the padding after the loop
    for i, line in enumerate(lines):
        line_list = []  # list of pipes or tuples of the form (ch, i, j)
        for j, ch in enumerate(line.strip()):
            if ch not in [".", "S"]:
                pipe = Pipe((i + 1, j + 1), ch)
                line_list.append(pipe)
            else:
                # line_list.append((ch, i + 1, j + 1))
                line_list.append(ch)
                if ch == "S":
                    starting_i, starting_j = (i + 1, j + 1)
        grid.append_row(line_list)
    grid.pad()
    return grid, starting_i, starting_j


@timeit
def solve_part1(grid, starting_i, starting_j):
    loop = find_loop(grid, starting_i, starting_j)
    ans_part1 = int((len(loop) + 1) / 2)
    return loop, ans_part1


@timeit(unit="s")
def solve_part2(grid, starting_i, starting_j, loop):
    starting_pipe = infer_start_pipe_type(starting_i, starting_j, loop[0], loop[-1])
    loop.append(starting_pipe)
    grid[starting_i, starting_j] = starting_pipe
    new_grid = scan(grid.content, loop)  # list of lists
    n_tiles_enclosed = sum(1 for row in new_grid for elem in row if elem == 2)
    return grid, n_tiles_enclosed


def main():
    grid, starting_i, starting_j = parse_input("../AoC-input/2023/day10.txt")

    loop, ans_part1 = solve_part1(grid, starting_i, starting_j)
    print(f"Part 1: {ans_part1}")

    grid, n_tiles_enclosed = solve_part2(grid, starting_i, starting_j, loop)
    print(f"Part 2: {n_tiles_enclosed}")


if __name__ == "__main__":
    main()
    # test_part1_example2()
