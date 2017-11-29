#TicTacToe.py
##Two player tic-tac-toe game
##Future extensions:
##  Computer player
##  Extend GUI to accomodate any size nxn game board

from TicTacToeInterface import GraphicInterface

class TicTacToe():
    """ Main application """

    def __init__(self, interface, n):
        self.interface = interface
        self.winner = ' '
        self.n = n #board size (nxn)
        self.maxTurns = self.n**2
        
    def checkWin(self, board, play):
        """ Check to see if a player has won """
        #if a turn hasn't been played yet, nobody can have won
        if board[play[0]][play[1]] == ' ':
            return False
        #check diagonals, rows, and columns
        win = (self.checkOneDiagonal(board, play) or
               self.checkTwoDiagonal(board, play) or
               self.checkRow(board, play) or
               self.checkColumn(board, play))
        #if somebody has won, flag that player as the winner
        if win:
            self.winner = board[play[0]][play[1]]
        return win

    def checkOneDiagonal(self, board, play):
        """ check for a win in first diagonal """
        #if the latest play wasn't on the diagonal, don't need to go thru with the check
        if play[0] != play[1]:
            return False
        #if any diagonal entry doesn't match the one before it, there's not a win
        for i in range(1, self.n):
            if board[i][i] != board[i-1][i-1]:
                return False
        #if all diagonal entries match, someone has won
        return True

    def checkTwoDiagonal(self, board, play):
        """ check for a win in second diagonal """
        #if the latest play wasn't on the diagonal, don't need to go thru with the check
        if play[0] != self.n-play[1]-1:
            return False
        #if any diagonal entry doesn't match the one before it, there's not a win
        for i in range(1, self.n):
            if board[i][self.n-i-1] != board[i-1][self.n-i]:
                return False
        #if all diagonal entries match, someone has won
        return True

    def checkRow(self, board, play):
        """ check for a win in the row last played """
        for i in range(1, self.n):
            if board[play[0]][i] != board[play[0]][i-1]:
                return False
        return True
    
    def checkColumn(self, board, play):
        """ check for in win in the column last played """
        for i in range(1, self.n):
            if board[i][play[1]] != board[i-1][play[1]]:
                return False
        return True
            
    def resetGame(self):
        """ reset everything to a fresh game """
        board = []
        for m in range(self.n):
            tempRow = []
            for n in range(self.n):
                tempRow.append(' ')
            board.append(tempRow)
        turn = 'x'
        self.winner = ' '
        turns = 0
        return board, turn, turns

    def run(self):
        """ Main gameplay method """
        board = []          #Initialize an empty game board
        for m in range(self.n):
            tempRow = []
            for n in range(self.n):
                tempRow.append(' ')
            board.append(tempRow)
        turn = 'x'          #Player x goes first
        gameQuit = False    #Flag indicating a player has quit
        turns = 0           #Count of turns played
        play = (0,0)        #Initialize first play for win checking

        #Keep taking turns until either board is full, someone wins, or someone quits
        while not gameQuit:
            while not (self.checkWin(board, play) or turns == self.maxTurns or gameQuit):
                turn, board, turns, play, gameQuit = self.interface.getInput(turn, board, turns)
            gameQuit = interface.gameEnd(board, self.winner, turn, gameQuit)
            board, turn, turns = self.resetGame()
        interface.close()


if __name__ == '__main__':
    n=50
    interface = GraphicInterface(n)
    theGame = TicTacToe(interface, n)
    theGame.run()


