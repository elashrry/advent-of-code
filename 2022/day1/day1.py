# part 1

max_calories = 0
with open("input.txt", "r") as f:
    elf_calories = 0
    for line in f:
        if line.strip() == "":
            if elf_calories > max_calories:
                max_calories = elf_calories
            elf_calories = 0
        else:
            cal = int(line.strip())
            elf_calories += cal
print("max calories:", max_calories)

# part 2

top_3_list = [0, 0, 0]
with open("input.txt", "r") as f:
    elf_calories = 0
    for line in f:
        if line.strip() == "":
            top_3_list = sorted(top_3_list + [elf_calories])[1:]
            elf_calories = 0
        else:
            cal = int(line.strip())
            elf_calories += cal
print("max calories with top 3 elves:", sum(top_3_list))