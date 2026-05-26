from tictic import TicTac


class Bool:
    def __init__(self) -> None:
        pass

    def bool(self):
        return True


class MajorBoard:
    def __init__(self, boards):
        self.current_board: int | None = None
        self.boards = boards
        self.wins = ["", "", "", "", "", "", "", "", ""]
        # self.b1 = boards[0]
        # self.b2 = boards[1]
        # self.b3 = boards[2]
        # self.b4 = boards[3]
        # self.b5 = boards[4]
        # self.b6 = boards[5]
        # self.b7 = boards[6]
        # self.b8 = boards[7]
        # self.b9 = boards[8]

    # def determine_board(self) -> int:
    # if self.current_board = None:
    #  input("which board")
    def __str__(self) -> str:
        self.print_self()
        return ""

    def print_unformatted(self):
        for board in self.boards:
            board.print_unformatted_tictac()

    def check_game(self):
        inc = 0
        for board in self.boards:
            if not not board.check_self():
                winner = board.check_self()
                print(f"{winner} has won a board.")
                self.wins[inc] = winner
            inc += 1

    def is_board_solved(self, board: int):
        if self.wins[board] != "":
            return True
        return False

    def is_self_board_solved_or_is_it_not_because_if_it_is_the_game_is_over(self):
        tic = TicTac()
        tic.board = [
            [self.wins[0], self.wins[1], self.wins[2]],
            [self.wins[3], self.wins[4], self.wins[5]],
            [self.wins[6], self.wins[7], self.wins[8]],
        ]
        return tic.check_self()
        # that was very eloquent i must say

    def give_board_num_from_coords(self, coordinates: tuple[str, int]):
        c = coordinates
        start: int = 0
        if c[1] < 4:
            start = 0
        elif c[1] < 7:
            start = 3
        else:
            start = 6
        if c[0] in ["D", "E", "F"]:
            start += 1
        if c[0] in ["G", "H", "I"]:
            start += 2
        return start

    def print_self(self):
        print("   A   B   C     D   E   F     G   H   I")
        print("              |             |           ")
        for x in range(9):
            print(f"{x + 1}  ", end="")
            if x <= 2:
                for i in range(3):
                    self.boards[i].print_row(x)
                    if i < 2:
                        print("  |  ", end="")
                print("")
                if x < 2:
                    print("  ----------  |  ---------  |  ----------")
                else:
                    print("              |             |           ")
                    print("  ------------|-------------|------------")
                    print("              |             |           ")
            elif x <= 5:
                xother = x - 3
                for i in range(3, 6):
                    self.boards[i].print_row(xother)
                    if i < 5:
                        print("  |  ", end="")
                print("")
                if x < 5:
                    print("  ----------  |  ---------  |  ----------")
                else:
                    print("              |             |           ")
                    print("  ------------|-------------|------------")
                    print("              |             |           ")
            elif x <= 8:
                xother = x - 6
                for i in range(6, 9):
                    self.boards[i].print_row(xother)
                    if i < 8:
                        print("  |  ", end="")
                print("")
                if x < 8:
                    print("  ----------  |  ---------  |  ----------")
                else:
                    print("              |             |           ")

    def change_cell(self, letter: str, number: int, change_to: str):
        """
        make sure the letters are lowercase thx
        """
        ascii = ord(letter)
        ascii -= 65
        number -= 1
        whichrow = compact_letter(number)
        whichboard = compact_letter(ascii)
        if whichrow == 0:
            self.boards[whichboard].board[number][ascii - (whichboard * 3)] = change_to
        elif whichrow == 1:
            self.boards[whichboard + 3].board[number - 3][ascii - (whichboard * 3)] = (
                change_to
            )
        else:
            self.boards[whichboard + 6].board[number - 6][ascii - (whichboard * 3)] = (
                change_to
            )

    def board_num_from_play(
        self, coord: tuple[str, int]
    ) -> int:  # why would it return a tuple
        """
        We return
        what no... num 0-8
        thats how my code works kboard number to go to next...
        """
        letter = coord[0]
        number = coord[1]

        ascii = ord(letter)
        ascii -= 65
        number -= 1
        whichrow = compact_letter(number)
        whichboard = compact_letter(ascii)
        if whichrow == 0:
            return file_for_bankruptcy(number, ascii - (whichboard * 3))
        elif whichrow == 1:
            return file_for_bankruptcy(number - 3, ascii - (whichboard * 3))
        else:
            return file_for_bankruptcy(number - 6, ascii - (whichboard * 3))

    # This is in the wrong spot? we need minor position from play in tictac? oooh maybe not i see
    def give_cool_little_hint(self, posi):
        if posi == None:
            return "You can play anywhere (well, almost)."
        hints = [
            "upper left",
            "upper middle",
            "upper right",
            "middle left",
            "direct middle",
            "middle right",
            "bottom left",
            "bottom middle",
            "bottom right",
        ]
        return f"You must play in the {hints[posi]} board."

    def cell_from_coords(self, coord: tuple[str, int]) -> str:
        letter = coord[0]
        number = coord[1]

        ascii = ord(letter)
        ascii -= 65
        number -= 1
        whichrow = compact_letter(number)
        whichboard = compact_letter(ascii)
        if whichrow == 0:
            return self.boards[whichboard].board[number][ascii - (whichboard * 3)]
        elif whichrow == 1:
            return self.boards[whichboard + 3].board[number - 3][
                ascii - (whichboard * 3)
            ]
        else:
            return self.boards[whichboard + 6].board[number - 6][
                ascii - (whichboard * 3)
            ]


def compact_letter(lett: int) -> int:
    if lett < 3:
        return 0
    elif lett < 6:
        return 1
    else:
        return 2


def file_for_bankruptcy(num: int, other: int) -> int:
    return (num * 3) + other
