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
        print("invalid len")
        return False  # noqa: E701
    if str(move[0]).upper() not in valid_letters:
        print("invalid letter")
        return False  # noqa: E701
    if str(move[1]) not in valid_nubmers:
        print("invalid number")
        return False
    if major_board.is_board_solved(
        major_board.give_board_num_from_coords((move[0], int(move[1])))
    ):
        print("board is already won")
        return False
    if major_board.cell_from_coords((move[0], int(move[1]))) != " ":
        return False
    if (
        correct_next_board is not None
        and major_board.give_board_num_from_coords((move[0], int(move[1])))
        != correct_next_board
    ):
        return False
    move = move[0].upper() + move[1:]
    return [move[0], int(move[1])]


def game_loop():
    global turn
    global correct_next_board
    print(f"{turn}'s move. {major_board.give_cool_little_hint(correct_next_board)}")
    move = input("Please enter coordinate move: ")
    submission = move
    checked_submission = check_input(submission)
    if not checked_submission:
        print("Invalid move")
    else:
        major_board.change_cell(checked_submission[0], checked_submission[1], turn)
        major_board.check_game()
        major_board.print_self()
        correct_next_board = major_board.board_num_from_play(
            (checked_submission[0], checked_submission[1])
        )
        if turn == "A":
            turn = "B"
        else:
            turn = "A"


if __name__ == "__main__":
    while not won:
        game_loop()
    print(f"Game over. {won} won.")
