from math import ceil

from aocutils import Parser
from aocutils import solve_quadratic_eqn


def parse_input(file_name):
    lines = Parser(file_name).get_lines()
    time_line = lines[0].split(": ")[1].strip()
    time_list = list(map(int, time_line.split()))
    record_line = lines[1].split(": ")[1].strip()
    record_list = list(map(int, record_line.split()))

    return time_list, record_list


def main():
    time_list, record_list = parse_input("../AoC-input/2023/day6.txt")
    # part 1: write distance formula --> quadratic equation to be solved
    answer = 1
    for total_time, record in zip(time_list, record_list):
        # assumption: real solutions always exist here
        sol1, sol2 = solve_quadratic_eqn(1, -total_time, record)
        # if sol1 is 1.5 or 2, we want to start from 2
        # if sol2 is 5.5 or 6, we want to finish at 5
        lower = ceil(max(0, sol1))
        upper = ceil(min(total_time, sol2))  # won't be included
        total_ways_to_win = len([t for t in range(lower, upper)])
        answer *= total_ways_to_win
    print("total ways to beat all records (part 1)", answer)

    # part 2: same idea just different numbers
    total_time_part_2 = int("".join([str(t) for t in time_list]))
    record_part_2 = int("".join([str(t) for t in record_list]))
    sol1, sol2 = solve_quadratic_eqn(1, -total_time_part_2, record_part_2)
    lower = ceil(max(0, sol1))
    upper = ceil(min(total_time_part_2, sol2))  # won't be included
    total_ways_to_win_part2 = len([t for t in range(lower, upper)])
    print("total ways to beat record (part 2)", total_ways_to_win_part2)


if __name__ == "__main__":
    main()
