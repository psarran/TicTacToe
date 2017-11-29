#TicTacToeTextInterface.py
## Interface for tic-tac-toe game

from graphics import *
from TicTacToeButton import Button, Tile
import math

class GraphicInterface():
    """ Graphic interface for tic-tac-toe game """

    def __init__(self, n):
        self.n = n
        self.win = GraphWin('Tic-Tac-Toe', 600, 400)
        self.win.setBackground('grey')
        screenW, screenH = 600, 400

        banner = Text(Point(300, 30), 'Tic-Tac-Toe')
        banner.setSize(24)
        banner.setStyle('bold')
        banner.draw(self.win)

        self.header = Text(Point(300, 55), 'Welcome')
        self.header.setSize(18)
        self.header.draw(self.win)

        self.drawBoard(screenW, screenH, self.win)
        
        self.startButton = Button(self.win, Point(200, 370), 100, 30, 'Start')
        self.quitButton = Button(self.win, Point(400, 370), 100, 30, 'Quit')
        self.startButton.activate()   #future update: will want to activate this only after user chooses an n
        self.quitButton.activate()

        self.firstGame = True

    def drawBoard(self, screenW, screenH, win):
        
        x, y = math.floor(screenW * 0.275), math.floor(screenH * 0.175) # (x,y) at top left of game board
        w, h = math.floor(screenW * 0.45),  math.floor(screenH * 0.675) # width/height of game board

        #Create vectors marking midpoints of each square on the game board
        xCoords, yCoords = [], []
        for i in range(self.n):
            xCoords.append(x + round(w/self.n/2) + round(i * w / self.n))
            yCoords.append(y + round(w/self.n/2) + round(i * h / self.n))

        #Create the clickable tiles centered in each square
        self.displayBoard = []
        #Midpoint of each playable square on the board
        for m in range(self.n):
            self.displayBoard.append([])
            for n in range(self.n):
                self.displayBoard[m].append(Tile(win, Point(xCoords[m], yCoords[n]), round(w/self.n), round(h/self.n)))

    def getClick(self):
        #wait for user to click on a button / tile
        #then return that button / tile
        while True:
            pt = self.win.getMouse()
            if self.startButton.clicked(pt):
                return 'Start'
            if self.quitButton.clicked(pt):
                return 'Quit'
            for m in range(self.n):
                for n in range(self.n):
                    if self.displayBoard[m][n].clicked(pt):
                        return (m, n)

    def gameEnd(self, board, winner, turn, gameQuit):
        if gameQuit: return True
        
        self.startButton.setLabel('Play Again')
        self.startButton.activate()

        for m in self.displayBoard:
            for n in m:
                n.deactivate()

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
        for m in self.displayBoard:
            for n in m:
                n.unDraw()
                n.activate()
                
    def getInput(self, turn, board, turns):
        if self.firstGame:
            click = self.getClick()
            if click == 'Quit':
                #shut down
                return turn, board, turns, (0,0), True
            elif click == 'Start':
                self.initiateGame()
                return turn, board, turns, (0,0), False
        else:
            self.header.setText('{0}\'s Turn'.format(turn.upper()))
            click = self.getClick()
            if click == 'Quit':
                return turn, board, turns, (0,0), True
            else:
                board[click[0]][click[1]] = turn
                turns += 1
                if turn == 'x':
                    self.displayBoard[click[0]][click[1]].drawX()
                    self.displayBoard[click[0]][click[1]].deactivate() #no longer playable
                    turn = 'o'
                else:
                    self.displayBoard[click[0]][click[1]].drawO()
                    self.displayBoard[click[0]][click[1]].deactivate() #no longer playable
                    turn = 'x'
                return turn, board, turns, click, False

    def close(self):
        self.win.close()

