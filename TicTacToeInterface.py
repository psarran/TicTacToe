#TicTacToeTextInterface.py
## Interface for tic-tac-toe game

from graphics import *
from TicTacToeButton import Button, Tile
import math

class GraphicInterface():
    """ Graphic interface for tic-tac-toe game """

    def __init__(self):
        self.win = GraphWin('Tic-Tac-Toe', 600, 400)
        self.win.setBackground('grey')
        self.screenW, self.screenH = 600, 400

        banner = Text(Point(300, 30), 'Tic-Tac-Toe')
        banner.setSize(24)
        banner.setStyle('bold')
        banner.draw(self.win)

        self.header = Text(Point(300, 55), 'Welcome')
        self.header.setSize(18)
        self.header.draw(self.win)

        self.startButton = Button(self.win, Point(200, 370), 100, 30, 'Start')
        self.quitButton = Button(self.win, Point(400, 370), 100, 30, 'Quit')
        self.startButton.activate()   #future update: will want to activate this only after user chooses an n
        self.quitButton.activate()

        self.firstGame = True

    def getGameSize(self):
        """ An interface to choose size of game board """
        screenW, screenH, win = self.screenW, self.screenH, self.win
        x, y = math.floor(screenW * 0.275), math.floor(screenH * 0.175) # (x,y) at top left of game board
        w, h = math.floor(screenW * 0.45),  math.floor(screenH * 0.675) # width/height of game board
        numRows, numColumns = 3, 5

        #Create vectors marking midpoints of each square option
        xCoords, yCoords = [], []
        for i in range(numColumns):
            xCoords.append(x + round(w/numColumns/2 + i * w / numColumns))
        for i in range(numRows):
            yCoords.append(y + round(w/numRows/2 + i * h / numRows))

        #Create buttons for each option centered in each square
        self.sizeChoices = []
        for i in range(numRows*numColumns):
            m = i % numColumns
            n = int((i-m)/numColumns)
            print(i, m, n, xCoords[m], yCoords[n])
            self.sizeChoices.append(Button(win, Point(xCoords[m], yCoords[n]), round(w/numColumns), round(h/numRows), '{0}'.format(i+2)))
            self.sizeChoices[i].activate()

        gameSizeChoice = 0
        startQuit = ' '
        while not (gameSizeChoice > 0 and (startQuit=='Quit' or startQuit=='Start')):
            click = self. getClick()
            if type(click) == int:
                if gameSizeChoice != 0: #unHighlight any previous selection
                    self.sizeChoices[gameSizeChoice-2].unHighlight()
                gameSizeChoice = click
                self.sizeChoices[click-2].highlight()
            if click == 'Quit':
                startQuit = click
            if gameSizeChoice > 0: #Can only start game if a choice has been made
                startQuit = click

        self.gameSize = gameSizeChoice

        if startQuit=='Start': # only draw the board if we're starting a game
            for m in range(numRows * numColumns):
                self.sizeChoices[m].unDraw()
            self.drawBoard(self.screenW, self.screenH, self.win)

        return gameSizeChoice, startQuit=='Quit'

    def drawBoard(self, screenW, screenH, win):
        x, y = math.floor(screenW * 0.275), math.floor(screenH * 0.175) # (x,y) at top left of game board
        w, h = math.floor(screenW * 0.45),  math.floor(screenH * 0.675) # width/height of game board

        #Create vectors marking midpoints of each square on the game board
        xCoords, yCoords = [], []
        for i in range(self.gameSize):
            xCoords.append(x + round(w/self.gameSize/2 + i * w / self.gameSize))
            yCoords.append(y + round(w/self.gameSize/2 + i * h / self.gameSize))

        #Create the clickable tiles centered in each square
        self.displayBoard = []
        for m in range(self.gameSize):
            self.displayBoard.append([])
            for n in range(self.gameSize):
                self.displayBoard[m].append(Tile(win, Point(xCoords[m], yCoords[n]), round(w/self.gameSize), round(h/self.gameSize)))

    def getClick(self):
        #wait for user to click on a button / tile
        #then return that button / tile
        while True:
            pt = self.win.getMouse()
            if self.startButton.clicked(pt):
                return 'Start'
            if self.quitButton.clicked(pt):
                return 'Quit'

            if self.firstGame:  #get clicks for game size
                for i in range(len(self.sizeChoices)):
                    if self.sizeChoices[i].clicked(pt):
                        return i+2
            else: #game board has been drawn so check for clicks there
                for m in range(self.gameSize):
                    for n in range(self.gameSize):
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
        self.drawBoard(self.screenW, self.screenH, self.win)
        for m in self.displayBoard:
            for n in m:
                n.unDraw()
                n.activate()

    def getInput(self, turn, board, turns, gameSize):
        if self.firstGame:
            self.gameSize = gameSize
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
