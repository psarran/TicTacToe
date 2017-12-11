#TicTacToe.py
##Two player tic-tac-toe game
##Future extensions:
##  Computer player
##  Extend GUI to accomodate any size nxn game board

from TicTacToeInterface import GraphicInterface

class TicTacToe():
    """ Main application """

    def __init__(self, interface):
        self.interface = interface

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
        for i in range(1, self.gameSize): #start at second diagonal because check looks back one
            if board[i][i] != board[i-1][i-1]:
                return False
        #if all diagonal entries match, someone has won
        return True

    def checkTwoDiagonal(self, board, play):
        """ check for a win in second diagonal """
        #if the latest play wasn't on the diagonal, don't need to go thru with the check
        if play[0] != self.gameSize-play[1]-1:
            return False
        #if any diagonal entry doesn't match the one before it, there's not a win
        for i in range(1, self.gameSize):
            if board[i][self.gameSize-i-1] != board[i-1][self.gameSize-i]:
                return False
        #if all diagonal entries match, someone has won
        return True

    def checkRow(self, board, play):
        """ check for a win in the row last played """
        for i in range(1, self.gameSize):
            if board[play[0]][i] != board[play[0]][i-1]:
                return False
        return True

    def checkColumn(self, board, play):
        """ check for in win in the column last played """
        for i in range(1, self.gameSize):
            if board[i][play[1]] != board[i-1][play[1]]:
                return False
        return True

    def resetGame(self):
        """ reset everything to a fresh game """
        board = self.buildBoard()
        turn = 'x'
        self.winner = ' '
        turns = 0
        return board, turn, turns

    def buildBoard(self):
        """ initialize an empty game board """
        board = []
        for m in range(self.gameSize):
            tempRow = []
            for n in range(self.gameSize):
                tempRow.append(' ')
            board.append(tempRow)
        return board

    def run(self):
        """ Main gameplay method """
        #Initialize game
        self.winner = ' '
        gameQuit = False    #Flag indicating a player has quit
        self.gameSize, gameQuit = self.interface.getGameSize() #board size (nxn)
        maxTurns = self.gameSize**2        #define max turns possible on board
        board = self.buildBoard()   #create an empty game board
        turn = 'x'          #Player x goes first
        turns = 0           #Count of turns played
        play = (0,0)        #Initialize first play for win checking

        #Keep taking turns until either board is full, someone wins, or someone quits
        while not gameQuit:
            while not (self.checkWin(board, play) or turns == maxTurns or gameQuit):
                turn, board, turns, play, gameQuit = self.interface.getInput(turn, board, turns, self.gameSize)
            gameQuit = interface.gameEnd(board, self.winner, turn, gameQuit)
            board, turn, turns = self.resetGame()
        self.interface.close()

if __name__ == '__main__':
    interface = GraphicInterface()
    theGame = TicTacToe(interface)
    theGame.run()
