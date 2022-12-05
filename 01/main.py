def problem_one(elf_calories: list[list[str]]) -> int:
    elf_calories = [[int(calorie) for calorie in elf] for elf in elf_calories]
    elf_calories_sum = [sum(calories) for calories in elf_calories]
    return max(elf_calories_sum)


def problem_two(input):
    pass


def main() -> None:
    with open('input.txt', 'r') as f:
        data = f.read()
    elf_calories = [item.split('\n') for item in data.split('\n\n')]
    p1_answer = problem_one(elf_calories)
    print(p1_answer)


if __name__ == '__main__':
    main()
