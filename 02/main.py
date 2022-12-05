# A is Rock, B is Paper, C is Scissor, X is Rock, Y Paper, Z Scissors.
# 1 Point for choosing rock, 2 points for paper, 3 for scissors.
# 0 points loss, 3 points draw, 6 points win


def problem_one(rps_groupings: list[list[str]]) -> int:
    """What would your total score be if everything goes exactly according to
    your strategy guide?
    """
    return sum([rps_schema(group[0], group[1]) for group in rps_groupings])


def problem_two():
    pass


def main() -> None:
    with open("input.txt", "r") as f:
        data = f.read()
    rps_groupings = [
        [group for group in item.split(" ")] for item in data.split("\n")
    ]
    p1_answer = problem_one(rps_groupings)
    print(p1_answer)


def rps_schema(opponent: str, ours: str) -> int:
    score: int = 0
    match ours:
        case "X":
            score += 1
            if opponent == "A":
                score += 3
            elif opponent == "B":
                pass
            elif opponent == "C":
                score += 6
        case "Y":
            score += 2
            if opponent == "A":
                score += 6
            elif opponent == "B":
                score += 3
            elif opponent == "C":
                pass
        case "Z":
            score += 3
            if opponent == "A":
                pass
            elif opponent == "B":
                score += 6
            elif opponent == "C":
                score += 3
    return score


if __name__ == "__main__":
    main()
