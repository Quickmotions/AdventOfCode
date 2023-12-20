class Scratchcard:
    def __init__(self, info) -> None:
        game_num, numbers = info.split(": ")
        game_num = game_num.split(" ")

        win_num, cur_num = numbers.split(" | ")
        win_num = list(filter(None, win_num.split(" ")))
        cur_num = list(filter(None, cur_num.split(" ")))

        self.card_no: int = game_num[-1]
        self.winning_numbers: list[int] = win_num
        self.numbers: list[int] = cur_num

    def get_value(self) -> int:
        amount_of_wins = 0
        for num in self.numbers:
            if num in self.winning_numbers:
                if amount_of_wins == 0:
                    amount_of_wins += 1
                else:
                    amount_of_wins *= 2
        return amount_of_wins


def run(data: list[str]):
    cards = []
    value = 0
    for card_info in data:
        cards.append(Scratchcard(card_info))

    for card in cards:
        print(f"card {card.card_no} : {card.get_value()}")
        value += card.get_value()
    print(f"Combined Total: {value}")


with open("2023/DayFour/input.txt") as f:
    array: list[str] = []
    for line in f.readlines():
        line = line.strip('\n')
        if line == '':
            continue
        array.append(line)
run(array)
