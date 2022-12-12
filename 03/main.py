from string import ascii_letters

priority_mapping = {l: i + 1 for i, l in enumerate(ascii_letters)}


def problem_one(data) -> int:
    result = 0
    for rucksack in data:
        letter = [
            i
            for i in rucksack[:len(rucksack) // 2]
            if i in rucksack[len(rucksack) // 2:]
        ]
        result += priority_mapping[letter[0]]

    return result


def problem_two(data) -> int:
    result = 0
    data = [data[i:i + 3] for i in range(0, len(data), 3)]
    for elf_group in data:
        letter = [
            i for i in elf_group[0] if i in elf_group[1] and i in elf_group[2]
        ]
        result += priority_mapping[letter[0]]

    return result


def main() -> None:
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f]
    print(problem_one(data))
    print(problem_two(data))


if __name__ == "__main__":
    main()
