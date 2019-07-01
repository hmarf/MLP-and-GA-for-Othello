from Board import Board
from Stone import Stone

class Othello:

    def __init__(self,nplay=1,show_result=False,show_board=False):

        self._nplay = nplay
        self._show_result = show_result
        self._show_board = show_board
        self.BLACK = Stone("●")
        self.WHITE = Stone("○")
        self.BLANK = Stone("×")
        self.OPPONENT = {self.BLACK: self.WHITE, self.WHITE: self.BLACK}

    def play(self,player1,player2):
        p1 = player1
        p2 = player2
        board = Board()
        while board.is_playable():
            x, y , stone = p1.play(board)
            if not( x == y == stone == 0):
                count = 0
                board.put(x,y,stone)
            (p1, p2) = (p2,p1)
        return self.show_result(board)

    def show_result(self, board):
        computer_stones = board.count(self.BLACK)
        user_stones = board.count(self.WHITE)
        if computer_stones > user_stones:
            return 3, 0
        elif computer_stones < user_stones:
            return 0, 3
        else:
            return 1, 1