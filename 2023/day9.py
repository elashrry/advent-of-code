from aocutils import Parser


def predict(history_list, direction="forward"):
    if direction not in ["forward", "backward"]:
        raise ValueError("direction can only be either 'forward' or 'backward'")
    if not history_list:
        return 0
    diff_seq_list = [
        history_list[i] - history_list[i - 1] for i in range(1, len(history_list))
    ]
    predict_value = history_list[-1] if direction == "forward" else history_list[0]
    if any(diff_seq_list):  # not all zeros
        if direction == "forward":
            predict_value += predict(diff_seq_list, direction=direction)
        else:
            predict_value -= predict(diff_seq_list, direction=direction)
    return predict_value


def main():
    integers = Parser("../AoC-input/2023/day9.txt").get_integers(sep=" ")
    total_forward = sum(predict(h_list, direction="forward") for h_list in integers)
    total_backward = sum(predict(h_list, direction="backward") for h_list in integers)

    print("The sum of extrapolated values (forward)", total_forward)
    print("The sum of extrapolated values (backward)", total_backward)


if __name__ == "__main__":
    main()
