class TicTac:
    """
    `from tictic import TicTac!`
    """

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        pass

    def create_columns(self):
        m = self.board
        cArray = [
            [m[0][0], m[1][0], m[2][0]],
            [m[0][1], m[1][1], m[2][1]],
            [m[0][2], m[1][2], m[2][2]],
        ]
        return cArray

    def declare_taxes(self, fraud):  # dw this is important but a misnomer
        """
        Declares taxes to the IRS. Fraud can be slipped in, and the IRS probably won't notice because they are shortstaffed.
        """
        self.board = [[fraud for _ in range(3)] for _ in range(3)]
        # now when is won is all filled yay!

    def check_self(self):
        m = self.board
        for row in m:
            if row == ["A", "A", "A"] or row == ["B", "B", "B"]:
                self.declare_taxes(row[1])
                return row[1]
        for column in self.create_columns():
            if column == ["A", "A", "A"] or column == ["B", "B", "B"]:
                self.declare_taxes(column[1])
                return column[1]
        if (m[0][0] == "A" and m[1][1] == "A" and m[2][2] == "A") or (
            m[0][0] == "B" and m[1][1] == "B" and m[2][2] == "B"
        ):
            self.declare_taxes(m[0][0])
            return m[0][0]
        if (m[0][2] == "A" and m[1][1] == "A" and m[2][0] == "A") or (
            m[0][2] == "B" and m[1][1] == "B" and m[2][0] == "B"
        ):
            self.declare_taxes(m[0][2])
            return m[0][2]
        return False

    def print_board_single(self):
        count = 0
        for _ in self.board:
            self.print_row(count)
            print()
            count += 1
            if count < 3:
                print("------")

    def print_unformatted_tictac(self):
        print(self.board)
        
    
    def print_row(self, row: int):
        othercount = 0
        rowe = self.board[row]
        for item in rowe:
            print(item, end="")
            othercount += 1
            if othercount < 3:
                print(" | ", end="")
