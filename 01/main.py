def problem_one(elf_calories: list[list[int]]) -> int:
    """Find the Elf carrying the most Calories, How many total Calories is
    that Elf carrying?
    """
    return max([sum(calories) for calories in elf_calories])


def problem_two(elf_calories: list[list[int]]) -> int:
    """Find the top three Elves carrying the most Calories. How many Calories
    are those Elves carrying in total?
    """
    return sum(
        sorted([sum(calories) for calories in elf_calories], reverse=True)[:3]
    )


def main() -> None:
    with open("input.txt", "r") as f:
        data = f.read()
    elf_calories = [
        [int(i) for i in item.split("\n") if i] for item in data.split("\n\n")
    ]
    p1_answer = problem_one(elf_calories)
    p2_answer = problem_two(elf_calories)
    print(
        f"Problem one answer is {p1_answer}. \n"
        f"Problem two answer is {p2_answer}."
    )


if __name__ == "__main__":
    main()
