#Luis Borja
#borjL
#3-8-2026
#Portfolio project involving making an animal game with two players using objects and methods.

class Piece:
    """
    Base class for all game pieces in AnimalGame. This class is the super/parent class
    and stores attributes like color and position.
    """
    def __init__(self, color, position):
        """
        Initializes the object with its color and starting position
        :param color: tangerine or amethyst
        :param position: algebraic position
        """
        self._color = color
        self._position = position

    def get_color(self):
        """
        Returns the color of the piece
        """
        return self._color

    def get_position(self):
        """
        Returns the current position of the piece
        """
        return self._position

    def set_position(self, position):
        """
        Sets the piece's current position after a move
        :param position: position to move the piece to
        :return: nothing
        """
        self._position = position

    def get_legal_moves(self, board):
        """
        Returns a list of all possible destinations based on the current state of the board
        :param board: is passed as an argument to check all possible moves
        :return: list of legal destinations in algebraic notation
        """
        pass

    def _pos_to_coords(self, position):
        """
        Converts an algebraic notation position to integers for board calculations.
        :param position: algebraic notation
        :return: integers
        """
        columns = "abcdefg"
        col = columns.index(position[0])
        row = int(position[1]) - 1
        return col, row


    def _coords_to_pos(self, col, row):
        """
        Converts integers back to algebraic notation
        :param col: column integer
        :param row: row integer
        :return: algebraic notation
        """
        columns = "abcdefg"
        col_letter = columns[col]
        row_number = str(row + 1)
        position = col_letter + row_number
        return position

class Pika(Piece):
    """
    Represents the Pika piece. Moves orthogonal, sliding, and distance of 4.
    Calculates all legal moves for the piece. Inherits from Piece parent class.
    """

    def __init__(self, color, position):
        """
        Initializes a Pika piece with color and position
        :param color: tangerine or amethyst
        :param position: starting position in algebraic notation
        """
        super().__init__(color, position)

    def get_legal_moves(self, board):
        """
        Returns all legal destination squares for this Pika piece on the current board.
        Slides up to 4 squares orthogonally, stops if blocked. Can move 1 square diagonally.
        :param board: passed as argument to check all possible moves
        :return: list of legal destinations in algebraic notation
        """
        legal_moves = []
        orthogonal_moves = [(0,1), (0,-1), (1,0), (-1,0)]
        diagonal_moves = [(1,1), (1,-1), (-1,1), (-1,-1)]
        col, row = self._pos_to_coords(self._position)

        for col_change, row_change in orthogonal_moves:
            for index in range(1,5):
                new_col = col + (col_change * index)
                new_row = row + (row_change * index)
                if new_col < 0 or new_row < 0 or new_col > 6 or new_row > 6:
                    break
                new_position = self._coords_to_pos(new_col, new_row)
                if board.get(new_position) is None:
                    legal_moves.append(new_position)
                elif board[new_position].get_color() != self._color:
                    legal_moves.append(new_position)
                    break
                else:
                    break
        for col_change, row_change in diagonal_moves:
            new_col = col + col_change
            new_row = row + row_change
            if new_col < 0 or new_row < 0 or new_col > 6 or new_row > 6:
                continue
            new_position = self._coords_to_pos(new_col, new_row)
            if board.get(new_position) is None:
                legal_moves.append(new_position)
            elif board[new_position].get_color() != self._color:
                legal_moves.append(new_position)
        return legal_moves


class Trilobite(Piece):
    """
    Represents the Trilobite piece. Moves diagonal, sliding, and a distance of 2.
    Calculates all legal moves for the piece. Inherits from Piece parent class.
    """
    def __init__(self, color, position):
        """
        Initializes a Trilobite piece with color and position
        :param color: tangerine or amethyst
        :param position: starting position in algebraic notation
        """
        super().__init__(color, position)

    def get_legal_moves(self, board):
        """
        Returns all legal destination squares for this Trilobite piece on the current board.
        Slides up to 2 squares diagonally, stopping if blocked. Can move 1 square orthogonally
        :param board: passed as argument to check all possible moves
        :return: list of all legal destinations in algebraic notation
        """

        legal_moves = []
        orthogonal_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        col, row = self._pos_to_coords(self._position)

        for col_change, row_change in diagonal_moves:
            for index in range(1, 3):
                new_col = col + (col_change * index)
                new_row = row + (row_change * index)
                if new_col < 0 or new_row < 0 or new_col > 6 or new_row > 6:
                    break
                new_position = self._coords_to_pos(new_col, new_row)
                if board.get(new_position) is None:
                    legal_moves.append(new_position)
                elif board[new_position].get_color() != self._color:
                    legal_moves.append(new_position)
                    break
                else:
                    break
        for col_change, row_change in orthogonal_moves:
            new_col = col + col_change
            new_row = row + row_change
            if new_col < 0 or new_row < 0 or new_col > 6 or new_row > 6:
                continue
            new_position = self._coords_to_pos(new_col, new_row)
            if board.get(new_position) is None:
                legal_moves.append(new_position)
            elif board[new_position].get_color() != self._color:
                legal_moves.append(new_position)
        return legal_moves

class Wombat(Piece):
    """
    Represents the Wombat piece. Moves orthogonal, jumping, and a distance of 1.
    Calculates all legal moves for the piece. Inherits from Piece parent class.
    """
    def __init__(self, color, position):
        """
        Initializes a Wombat piece with color and position
        :param color: tangerine or amethyst
        :param position: starting position in algebraic notation
        """
        super().__init__(color, position)

    def get_legal_moves(self, board):
        """
        Returns all legal destination squares for this Wombat piece on the current board.
        Moves 1 square orthogonally or 1 square diagonally.
        :param board: passed as argument to check all possible moves
        :return: list of all legal destinations in algebraic notation
        """

        legal_moves = []
        orthogonal_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        col, row = self._pos_to_coords(self._position)

        for col_change, row_change in orthogonal_moves:
            new_col = col + col_change
            new_row = row + row_change
            if new_col < 0 or new_row < 0 or new_col > 6 or new_row > 6:
                continue
            new_position = self._coords_to_pos(new_col, new_row)
            if board.get(new_position) is None:
                legal_moves.append(new_position)
            elif board[new_position].get_color() != self._color:
                legal_moves.append(new_position)
        for col_change, row_change in diagonal_moves:
            new_col = col + col_change
            new_row = row + row_change
            if new_col < 0 or new_row < 0 or new_col > 6 or new_row > 6:
                continue
            new_position = self._coords_to_pos(new_col, new_row)
            if board.get(new_position) is None:
                legal_moves.append(new_position)
            elif board[new_position].get_color() != self._color:
                legal_moves.append(new_position)
        return legal_moves

class Beluga(Piece):
    """
    Represents the Beluga piece. Moves diagonal, jumping and a distance of 3.
    Calculates all legal moves for the piece. Inherits from Piece parent class.
    """
    def __init__(self, color, position):
        """
        Initializes a Beluga piece with color and position
        :param color: tangerine or amethyst
        :param position: starting position in algebraic notation
        """
        super().__init__(color, position)

    def get_legal_moves(self, board):
        """
        Returns all legal destination squares for this Beluga piece on the current board.
        Jumps 3 squares diagonally and cannot be blocked, or moves 1 square orthogonally.
        :param board: passed as argument to check all possible moves
        :return: list of all legal destinations in algebraic notation
        """

        legal_moves = []
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        orthogonal_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        col, row = self._pos_to_coords(self._position)

        for col_change, row_change in orthogonal_moves:
            new_col = col + col_change
            new_row = row + row_change
            if new_col < 0 or new_row < 0 or new_col > 6 or new_row > 6:
                continue
            new_position = self._coords_to_pos(new_col, new_row)
            if board.get(new_position) is None:
                legal_moves.append(new_position)
            elif board[new_position].get_color() != self._color:
                legal_moves.append(new_position)
        for col_change, row_change in diagonal_moves:
            new_col = col + (col_change * 3)
            new_row = row + (row_change * 3)
            if new_col < 0 or new_row < 0 or new_col > 6 or new_row > 6:
                continue
            new_position = self._coords_to_pos(new_col, new_row)
            if board.get(new_position) is None:
                legal_moves.append(new_position)
            elif board[new_position].get_color() != self._color:
                legal_moves.append(new_position)
        return legal_moves

class AnimalGame:
    """
    The actual game class. Manages the state of the board game. Initializes board and all
    starting pieces in their starting locations, tracks whose turn it is, checks if moves
    are legal, checks for win conditions and reports game state.
    """
    def __init__(self):
        """
        Initializes the game board, places all pieces in starting locations, sets turn to
        tangerine and game state to UNFINISHED
        """
        self._board = {}
        self._turn = "tangerine"
        self._game_state = "UNFINISHED"
        self._setup_board()

    def _setup_board(self):
        """
        Places all tangerine and amethyst pieces on the board in their starting positions.
        Places pieces in order and tangerine in row 1, amethyst row 7. Called once.
        :return: None
        """
        piece_order = [Pika, Trilobite, Wombat, Beluga, Wombat, Trilobite, Pika]
        for index, piece_type in enumerate(piece_order):
            tangerine_pos = self._coords_to_pos(index, 0)
            amethyst_pos = self._coords_to_pos(index, 6)
            self._board[tangerine_pos] = piece_type("tangerine", tangerine_pos)
            self._board[amethyst_pos] = piece_type("amethyst", amethyst_pos)

    def _pos_to_coords(self, position):
        """
        Converts an algebraic notation position to integers for board calculations.
        :param position: algebraic notation
        :return: integers
        """
        columns = "abcdefg"
        col = columns.index(position[0])
        row = int(position[1]) - 1
        return col, row


    def _coords_to_pos(self, col, row):
        """
        Converts integers back to algebraic notation
        :param col: column integer
        :param row: row integer
        :return: algebraic notation
        """
        columns = "abcdefg"
        col_letter = columns[col]
        row_number = str(row + 1)
        position = col_letter + row_number
        return position

    def get_game_state(self):
        """
        Returns the current state of the game
        :return: one of either UNFINISHED, TANGERINE_WON, AMETHYST_WON
        """
        return self._game_state

    def make_move(self, from_pos, to_pos):
        """
        Attempts to move a piece from_pos to to_pos. Checks that the game is still ongoing,
        that current piece belongs to the current player, and to_pos is a legal move.
        If valid, executes the move. Checks for Beluga capture and updates game state.
        Advances the turn
        :param from_pos: algebraic notation for the position moving from
        :param to_pos: algebraic notation for the position moving to
        :return: True if the move was made, False otherwise
        """
        if self._game_state != "UNFINISHED":
            return False
        if self._board.get(from_pos) is None:
            return False
        piece = self._board[from_pos]
        if piece.get_color() != self._turn:
            return False
        if to_pos not in piece.get_legal_moves(self._board):
            return False

        captured_piece = self._board.get(to_pos)
        self._board[to_pos] = piece
        self._board[from_pos] = None
        piece.set_position(to_pos)

        if isinstance(captured_piece, Beluga):
            if captured_piece.get_color() == "amethyst":
                self._game_state = "TANGERINE_WON"
            else:
                self._game_state = "AMETHYST_WON"
        if self._turn == "tangerine":
            self._turn = "amethyst"
        else:
            self._turn = "tangerine"
        return True

    def print_board(self):
        """
        Prints a visual of the current board state to visualize the flow of the game.
        Each occupied square shows the piece type and color.
        :return: None
        """
        for rows in range(6, -1, -1):
            row_string = ""
            for columns in range(0, 7):
                position = self._coords_to_pos(columns, rows)
                piece = self._board.get(position)
                if piece is None:
                    row_string += "-- "
                else:
                    color = piece.get_color()[0].upper()
                    piece_type = type(piece).__name__[0].upper()
                    row_string += color + piece_type + " "
            print(row_string)
if __name__ == "__main__":
    game = AnimalGame()
    game.print_board()

    while game.get_game_state() == "UNFINISHED":
        print(f"\n{game._turn.capitalize()}'s turn")
        from_pos = input("Move from: ").strip().lower()
        to_pos = input("Move to: ").strip().lower()

        if game.make_move(from_pos, to_pos):
            game.print_board()
        else:
            print("Invalid move, try again.")

    print(f"\nGame over! {game.get_game_state()}")