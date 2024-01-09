import re

from aocutils import Parser, timeit


@timeit
def solve_part1(parser):
    part1_regex = re.compile(r"\d")
    digits_found = parser.apply_regex(part1_regex)
    total = 0
    for line_digits in digits_found:
        cal_value = 10*int(line_digits[0]) + int(line_digits[-1])
        total += cal_value
    return total


@timeit
def solve_part2(parser):
    alphabet_digits = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, 
        "six": 6, "seven": 7, "eight": 8, "nine": 9,
        }
    part2_regex = re.compile(r"(?=(" + "|".join(alphabet_digits.keys()) + r"|\d))")
    digits_found = parser.apply_regex(part2_regex)
    total = 0
    for line_digits in digits_found:
        first_digit = alphabet_digits.get(line_digits[0], line_digits[0])
        second_digit = alphabet_digits.get(line_digits[-1], line_digits[-1])
        cal_value = 10*int(first_digit) + int(second_digit)
        total += cal_value
    return total


def main():
    parser = Parser("../AoC-input/2023/day1.txt")
    # part 1
    total = solve_part1(parser)
    print("the sum of all of the calibration values:", total)
    
    # part2
    total = solve_part2(parser)
    print("the _corrected_ sum of all of the calibration values:", total)


if __name__ == "__main__":
    main()
