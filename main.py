from morebad import MajorBoard
from tictic import TicTac

# def test_tictac():
#   tictac = TicTac()
#  tictac.print_board()
boards = []
for i in range(9):
    newBoard = TicTac()
    boards.append(newBoard)
won: str | bool = False

major_board = MajorBoard(boards)
major_board.print_self()


turn = "A"
correct_next_board: int | None = None
valid_letters = "ABCDEFGHI"
valid_nubmers = "123456789"


def check_input(move):

    if len(move) != 2:
        print(
            "Please do a valid coordinate. Like A1 or B7. Don't add anything else. Or remove anything I suppose."
        )
        return False  # noqa: E701
    if str(move[0]).upper() not in valid_letters:
        print("Please do a valid coordinate. Like A1 or B7.")
        return False  # noqa: E701
    if str(move[1]) not in valid_nubmers:
        print("Please do a valid coordinate. Like A1 or B7.")
        return False

    if major_board.cell_from_coords((move[0], int(move[1]))) != " ":
        return False
    if (
        correct_next_board is not None
        and major_board.give_board_num_from_coords((move[0], int(move[1])))
        != correct_next_board
    ):
        print("So, like, that's the wrong board. Play on the right one please.")
        return False
    if major_board.is_board_solved(
        major_board.give_board_num_from_coords((move[0], int(move[1])))
    ):
        print("Yeah so somebody already won that board. No idea who.")
        return False
    move = move[0].upper() + move[1:]
    return [move[0], int(move[1])]


def game_loop():
    global turn
    global correct_next_board
    global won
    print(f"{turn}'s move. {major_board.give_cool_little_hint(correct_next_board)}")
    move = input("Please enter coordinate move: ")
    if move[0]:
        move = move[0].upper() + move[1:]
    print("")
    submission = move
    checked_submission = check_input(submission)
    if not checked_submission:
        pass
    else:
        major_board.change_cell(checked_submission[0], checked_submission[1], turn)
        major_board.check_game()
        if major_board.is_self_board_solved_or_is_it_not_because_if_it_is_the_game_is_over():
            won = major_board.is_self_board_solved_or_is_it_not_because_if_it_is_the_game_is_over()
            print(won)
        major_board.print_self()
        correct_next_board = major_board.board_num_from_play(
            (checked_submission[0], checked_submission[1])
        )
        if major_board.is_board_solved(correct_next_board):
            correct_next_board = None
        if turn == "A":
            turn = "B"
        else:
            turn = "A"


if __name__ == "__main__":
    while not won:
        game_loop()
    print(f"Game over. {won} won.")
