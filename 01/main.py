def problem_one(elf_calories: list[list[str]]) -> int:
    """Find the Elf carrying the most Calories, How many total Calories is
    that Elf carrying?
    """
    elf_calories = [[int(calorie) for calorie in elf] for elf in elf_calories]
    elf_calories_sum = [sum(calories) for calories in elf_calories]
    return max(elf_calories_sum)


def problem_two(elf_calories: list[list[str]]) -> int:
    """Find the top three Elves carrying the most Calories. How many Calories
    are those Elves carrying in total?
    """
    elf_calories = [[int(calorie) for calorie in elf] for elf in elf_calories]
    elf_calories_sum = [sum(calories) for calories in elf_calories]
    elf_calories_sum.sort(reverse=True)
    return sum(elf_calories_sum[:3])


def main() -> None:
    with open('input.txt', 'r') as f:
        data = f.read()
    elf_calories = [item.split('\n') for item in data.split('\n\n')]
    p1_answer = problem_one(elf_calories)
    p2_answer = problem_two(elf_calories)
    print(f'Problem one answer is {p1_answer}. \n'
          f'Problem two answer is {p2_answer}.')


if __name__ == '__main__':
    main()
