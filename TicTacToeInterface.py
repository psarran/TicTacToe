#TicTacToeTextInterface.py
## Interface for tic-tac-toe game

from graphics import *
from TicTacToeButton import Button, Tile

class GraphicInterface():
    """ Graphic interface for tic-tac-toe game """

    def __init__(self):
        self.win = GraphWin('Tic-Tac-Toe', 600, 400)
        self.win.setBackground('grey')

        banner = Text(Point(300, 30), 'Tic-Tac-Toe')
        banner.setSize(24)
        banner.setStyle('bold')
        banner.draw(self.win)

        self.header = Text(Point(300, 55), 'Welcome')
        self.header.setSize(18)
        self.header.draw(self.win)

        Line(Point(255, 70), Point(255, 340)).draw(self.win)
        Line(Point(345, 70), Point(345, 340)).draw(self.win)
        Line(Point(165, 160), Point(435, 160)).draw(self.win)
        Line(Point(165, 250), Point(435, 250)).draw(self.win)

        self.displayBoard = []
        #Midpoint of each playable square on the board
        boardCoords = [(210, 115), (300, 115), (390, 115),
                       (210, 205), (300, 205), (390, 205),
                       (210, 295), (300, 295), (390, 295)]
        for i in range(9):
            self.displayBoard.append(Tile(self.win, Point(boardCoords[i][0], boardCoords[i][1]), 90, 90))

        self.startButton = Button(self.win, Point(200, 370), 100, 30, 'Start')
        self.quitButton = Button(self.win, Point(400, 370), 100, 30, 'Quit')
        self.startButton.activate()
        self.quitButton.activate()

        self.firstGame = True


    def getClick(self):
        #wait for user to click on a button / tile
        #then return that button / tile
        while True:
            pt = self.win.getMouse()
            if self.startButton.clicked(pt):
                return 'Start'
            if self.quitButton.clicked(pt):
                return 'Quit'
            for t in range(9):
                if self.displayBoard[t].clicked(pt):
                    return t

    def gameEnd(self, board, winner, turn, gameQuit):
        if gameQuit: return True
        
        self.startButton.setLabel('Play Again')
        self.startButton.activate()

        for t in self.displayBoard:
            t.deactivate()

        if winner == ' ':
            #If there's no winner, it's a tie
            self.header.setText('Game Over - Scratch')
        else:
            self.header.setText('{0} Wins!'.format(winner.upper()))

        click = self.getClick()
        if click == 'Quit':
            return True
        else:
            self.initiateGame()
            return False

    def initiateGame(self):
        self.firstGame = False
        self.startButton.deactivate()
        for t in self.displayBoard:
            t.unDraw()
            t.activate()
        
                
    def getInput(self, turn, board):
        if self.firstGame:
            click = self.getClick()
            if click == 'Quit':
                #shut down
                return turn, board, True
            elif click == 'Start':
                self.initiateGame()
                return turn, board, False
        else:
            self.header.setText('{0}\'s Turn'.format(turn.upper()))
            click = self.getClick()
            if click == 'Quit':
                return turn, board, True
            else:
                board[click] = turn
                if turn == 'x':
                    self.displayBoard[click].drawX()
                    self.displayBoard[click].deactivate() #no longer playable
                    turn = 'o'
                else:
                    self.displayBoard[click].drawO()
                    self.displayBoard[click].deactivate() #no longer playable
                    turn = 'x'
                return turn, board, False

    def close(self):
        self.win.close()

