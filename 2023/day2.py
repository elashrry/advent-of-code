import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def get_max_possible(game_line: str, color: str):
    # will be str like "1 red, 5 red"
    color_info_str = ",".join(re.findall(r"\d+ " + color, game_line))
    color_number_list = [
        int(digit) for digit in color_info_str.replace(color, "").split(",")
    ]
    return max(color_number_list)


def is_possible_game(
    max_possible_red: int, max_possible_green: int, max_possible_blue: int
):
    return (
        (max_possible_red <= MAX_RED)
        and (max_possible_green <= MAX_GREEN)
        and (max_possible_blue <= MAX_BLUE)
    )


def main():
    with open("../AoC-input/2023/day2.txt", "r") as f:
        power_sum = 0
        game_id_sum = 0
        for line in f:
            game_name = re.findall(r"Game \d+", line)[0]
            game_id = int(game_name.split(" ")[1])
            max_red_found = get_max_possible(line, "red")
            max_green_found = get_max_possible(line, "green")
            max_blue_found = get_max_possible(line, "blue")
            # part 1
            if is_possible_game(max_red_found, max_green_found, max_blue_found):
                game_id_sum += game_id
            # part 2
            power_sum += max_red_found * max_green_found * max_blue_found

    print("The sum of the IDs of possible games", game_id_sum)
    print("The sum of the power of minimal sets", power_sum)


if __name__ == "__main__":
    main()
