def predict(history_list, direction="forward"):
    if direction not in ["forward", "backward"]:
        raise ValueError("direction can only be either 'forward' or 'backward'")
    if not history_list:
        return 0
    diff_seq_list = [
        history_list[i] - history_list[i-1] for i in range(1, len(history_list))
        ]
    print(diff_seq_list)
    predict_value = history_list[-1] if direction=="forward" else history_list[0]
    n_zero = sum(d==0 for d in diff_seq_list)
    print("n zero", n_zero)
    if n_zero < len(diff_seq_list):
        if direction=="forward":
            predict_value += predict(diff_seq_list, direction=direction)
        else:
            predict_value -= predict(diff_seq_list, direction=direction)
    return predict_value

# part 1 & 2
with open("../AoC-input/2023/day9.txt", "r") as f:
    total_forward = 0
    total_backward = 0
    for line in f:
        history_list = list(map(int, line.strip().split()))
        print(history_list)
        value_forward = predict(history_list, direction="forward")
        value_backward = predict(history_list, direction="backward")
        total_forward += value_forward
        total_backward += value_backward

    print("The sum of extrapolated values (forward)", total_forward)
    print("The sum of extrapolated values (backward)", total_backward)
