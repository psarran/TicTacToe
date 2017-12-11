#TicTacToeButton.py
## Button and Tile objects used for the TicTacToe graphic interface

from graphics import *

class Button():
    """ Buttons for players to interact with the game """

    def __init__(self, win, center, width, height, label):
        """ Create button object which consists of a Rectangle centered at 'center'
            with a Text object with text 'label' """
        w, h = width/2, height/2
        x, y = center.getX(), center.getY()
        self.xmin, self.ymin = x-w, y-h
        self.xmax, self.ymax = x+w, y+h

        pt1 = Point(self.xmin, self.ymin)
        pt2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(pt1, pt2)

        self.label = Text(center,label)
        self.label.setTextColor('lightgrey')

        self.rect.draw(win)
        self.label.draw(win)
        self.deactivate()

    def activate(self):
        """ sets to active / available to be clicked """
        self.label.setTextColor('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """ sets to inactive / unavailable to be clicked """
        self.label.setTextColor('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def clicked(self, pt):
        """ if button is active this will determine if there was a click
            (pt) within the button """
        return (self.active and self.xmin <= pt.getX() <= self.xmax
                            and self.ymin <= pt.getY() <= self.ymax)

    def highlight(self):
        """ highlight / switch to 'selected' """
        self.rect.setWidth(4)

    def unHighlight(self):
        """ unhighlight / switch to 'not selected' """
        self.rect.setWidth(2)

    def getLabel(self):
        """ returns the label text """
        return self.label.getText()

    def setLabel(self, text):
        """ changes the label text """
        self.label.setText(text)

    def unDraw(self):
        """ undraw the button """
        self.rect.undraw()
        self.label.undraw()


class Tile():
    """ Objects used to represent the playable parts of the game board """

    def __init__(self, win, center, width, height):
        """ Create blank Tile object which consists of a Rectangle centered at 'center'
            with and a Circle and X that can be activated when played """
        w, h = width/2, height/2
        x, y = center.getX(), center.getY()
        self.xmin, self.ymin = x-w, y-h
        self.xmax, self.ymax = x+w, y+h

        pt1 = Point(self.xmin, self.ymin)
        pt2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(pt1, pt2)
        self.rect.draw(win)
        self.rect.setOutline('grey')
        self.rect.setFill('light grey')

        self.deactivate()

        self.center = center
        self.win = win

        self.markOne = Circle(self.center, (self.xmax-self.xmin)/2*.8)
        self.markTwo = self.markOne

    def drawX(self):
        """ draws an X """
        f = (self.xmax - self.xmin) * .1
        x1, y1, x2, y2 = self.xmin+f, self.ymin+f, self.xmax-f, self.ymax-f
        self.markOne = Line(Point(x1,y1), Point(x2,y2))
        self.markTwo = Line(Point(x2,y1), Point(x1,y2))
        self.markOne.draw(self.win)
        self.markTwo.draw(self.win)

    def drawO(self):
        """ draws an O """
        self.markOne = Circle(self.center, (self.xmax-self.xmin)/2*.8)
        self.markTwo = self.markOne
        self.markOne.draw(self.win)

    def unDraw(self):
        self.markOne.undraw()
        self.markTwo.undraw()

    def activate(self):
        """ sets to active / available to be clicked """
        self.active = True

    def deactivate(self):
        """ sets to inactive / unavailable to be clicked """
        self.active = False

    def clicked(self, pt):
        """ if button is active this will determine if there was a click
            (pt) within the button """
        return (self.active and self.xmin <= pt.getX() <= self.xmax
                            and self.ymin <= pt.getY() <= self.ymax)
