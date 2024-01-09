from aocutils import Parser, IntInterval, Subset, Mapper, timeit


@timeit
def get_last_output(input_subset, mapper_dict):
    """Performs a series of mappings on an input subset using a dictionary of mappers.

    The order of mapping is the natural order of keys in the ``dict``.

    Args:
        input_subset (Subset): The initial subset to start the mapping process.
        mapper_dict (dict): A dictionary containing mappers to be applied sequentially.

    Returns:
        (Subset): The final subset obtained after applying all the mappers.
    """
    sorted_key_list = sorted(list(mapper_dict.keys()))
    intermediate_output = input_subset
    for key in sorted_key_list:
        intermediate_output = mapper_dict[key].map(intermediate_output)
    return intermediate_output


def parse_input(file_name):
    parser = Parser(file_name)
    section_list = parser.get_sections()
    seed_line = section_list[0].strip()
    seed_pair_list = list(map(int, seed_line.split(": ")[1].strip().split()))
    start_values = seed_pair_list[::2]
    width_values = seed_pair_list[1::2]
    seed_subset_part1 = Subset(IntInterval(i, i + 1) for i in seed_pair_list)
    seed_subset_part2 = Subset(
        IntInterval(i, i + j) for i, j in zip(start_values, width_values)
    )
    mapper_dict = {}
    mapper_index = 0  # mapper index to make sure we go in same order
    for section in section_list[1:]:
        domain = []  # will be list of IntIntervals
        image = []
        mapper_map = {}
        i = 0
        for line in section.split("\n"):
            if "map" in line:
                map_key = str(mapper_index) + "-" + line.split()[0]
                continue
            image_start, domain_start, width = tuple(map(int, line.strip().split()))
            domain.append(IntInterval(domain_start, domain_start + width))
            image.append(IntInterval(image_start, image_start + width))
            mapper_map.update({domain_start: image_start})
            i += 1
        assert len(domain) == len(image) == i
        mapper_dict[map_key] = Mapper(Subset(domain), Subset(image), mapper_map)
        mapper_index += 1

    return seed_subset_part1, seed_subset_part2, mapper_dict


def main():
    file_name = "../AoC-input/2023/day5.txt"
    seed_subset_part1, seed_subset_part2, mapper_dict = parse_input(file_name)
    location_IntIntervals_part1 = get_last_output(seed_subset_part1, mapper_dict)
    location_IntIntervals_part2 = get_last_output(seed_subset_part2, mapper_dict)
    # subsets are ordered
    print("Closest location for part 1:", location_IntIntervals_part1[0].start)
    print("Closest location for part 2:", location_IntIntervals_part2[0].start)


if __name__ == "__main__":
    main()
