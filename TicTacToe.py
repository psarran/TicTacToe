#TicTacToe.py
##Two player tic-tac-toe game
##Future extensions:
##  Allow multiple games
##  Computer player

from TicTacToeInterface import GraphicInterface

class TicTacToe():
    """ Main application """

    def __init__(self, interface):
        self.interface = interface
        self.defineWins()  #Define win conditions
        self.winner = ' '

    def defineWins(self):
        """ Define win conditions """
        self.wins = [(0,1,2), (3,4,5), (6,7,8),
                     (0,3,6), (1,4,7), (2,5,8),
                     (0,4,8), (2,4,6)]

    def checkFull(self, board):
        """ Check to see if there are any empty places to play """
        full = True
        for i in board:
            if i == ' ': full = False
        return full

    def checkWin(self, board):
        """ Check to see if a player has won """
        for w in self.wins:
            if board[w[0]] != ' ' and (board[w[0]] == board[w[1]] == board[w[2]]):
                self.winner = board[w[0]]
                return True
            
    def resetGame(self):
        board = [' ']*9
        turn = 'x'
        self.winner = ' '
        return board, turn

    def run(self):
        """ Main gameplay method """
        board = [' ']*9     #Initialize an empty game board
        turn = 'x'          #Player x goes first
        gameQuit = False    #Flag indicating a player has quit

        #Keep taking turns until either board is full, someone wins, or someone quits
        while not gameQuit:
            while not (self.checkWin(board) or self.checkFull(board) or gameQuit):
                turn, board, gameQuit = self.interface.getInput(turn, board)
            gameQuit = interface.gameEnd(board, self.winner, turn, gameQuit)
            board, turn = self.resetGame()
        interface.close()


if __name__ == '__main__':
    interface = GraphicInterface()
    theGame = TicTacToe(interface)
    theGame.run()


