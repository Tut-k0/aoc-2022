# A is Rock, B is Paper, C is Scissor, X is Rock, Y Paper, Z Scissors.
# 1 Point for choosing rock, 2 points for paper, 3 for scissors.
# 0 points loss, 3 points draw, 6 points win


def problem_one(rps_groupings: list[list[str]]) -> int:
    """What would your total score be if everything goes exactly according to
    your strategy guide?
    """
    scores = []
    for group in rps_groupings:
        score = 0
        match group[1]:
            case "X":
                score += 1
                if group[0] == "A":
                    score += 3
                elif group[0] == "B":
                    pass
                elif group[0] == "C":
                    score += 6
            case "Y":
                score += 2
                if group[0] == "A":
                    score += 6
                elif group[0] == "B":
                    score += 3
                elif group[0] == "C":
                    pass
            case "Z":
                score += 3
                if group[0] == "A":
                    pass
                elif group[0] == "B":
                    score += 6
                elif group[0] == "C":
                    score += 3
        scores.append(score)

    return sum(scores)


# For problem 2, X means I need to lose, Y draw, and Z win.
# 1 Point for choosing rock, 2 points for paper, 3 for scissors.
# 0 points loss, 3 points draw, 6 points win
def problem_two(rps_groupings: list[list[str]]):
    """Following the Elf's instructions for the second column, what would your
    total score be if everything goes exactly according to your strategy guide?
    """
    scores = []
    for group in rps_groupings:
        score = 0
        match group[1]:
            case "X":
                if group[0] == "A":
                    score += 3
                elif group[0] == "B":
                    score += 1
                elif group[0] == "C":
                    score += 2
            case "Y":
                if group[0] == "A":
                    score += 4
                elif group[0] == "B":
                    score += 5
                elif group[0] == "C":
                    score += 6
            case "Z":
                if group[0] == "A":
                    score += 8
                elif group[0] == "B":
                    score += 9
                elif group[0] == "C":
                    score += 7
        scores.append(score)

    return sum(scores)


def main() -> None:
    with open("input.txt", "r") as f:
        data = f.read()
    rps_groupings = [
        [group for group in item.split(" ")] for item in data.split("\n")
    ]
    p1_answer = problem_one(rps_groupings)
    p2_answer = problem_two(rps_groupings)
    print(
        f"Problem one answer is {p1_answer}. \n"
        f"Problem two answer is {p2_answer}."
    )


if __name__ == "__main__":
    main()
