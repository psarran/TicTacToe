#TicTacToeTextInterfaceText.py
## Text-based interface for tic-tac-toe game

class TextInterface():
    """ Text based interface for Tic-Tac-Toe game """
    
    def __init__(self):
        pass

    def showBoard(self, board):
        """ Method to display current state of the game """

        #Create the list to display current plays plus an index for empty spots
        self.displayBoard = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(9):
            if board[i] != ' ':
                self.displayBoard[i] = board[i]

        #Display the current game board
        print('{0:^3}  {1:^3}  {2:^3}'
              .format(self.displayBoard[0],self.displayBoard[1], self.displayBoard[2]))
        print('{0:^3}  {1:^3}  {2:^3}'
              .format(self.displayBoard[3],self.displayBoard[4], self.displayBoard[5]))
        print('{0:^3}  {1:^3}  {2:^3}'
              .format(self.displayBoard[6],self.displayBoard[7], self.displayBoard[8]))

    def checkPlay(self, play, board):
        """ Check to see if the play matches one of the empty spots """
        validPlay = False
        if play == '': #Enter is a valid play
            validPlay = True
        else:
            for i in self.displayBoard:
                if int(play) == i: validPlay = True
        return validPlay

    def gameEnd(self, board, winner, turn, gameQuit):
        if gameQuit:
            print('\n', 'Player {0} forfeits. Game over.'.format(turn))
        elif winner == ' ':
            print('\n')
            self.showBoard(board)
            print('\nGame Over - Scratch')
        else:
            print('\n')
            self.showBoard(board)
            print('\nGame Over - {0} wins!'.format(winner.upper()))
            
    def getInput(self, turn, board):
        """ The main user interaction method """

        #Show current board and solicit an input from player
        print('\n\nCurrent board layout:\n')
        self.showBoard(board)
        print('\n{0}\'s turn'.format(turn.upper()), '\n')
        play = input('Type # indicating where you want to play (\'Enter\' to quit):')

        #Keep requesting an input until player makes a valid choice or quits
        while not self.checkPlay(play, board):
            play = input('Invalid play, try again:')

        
        if play == '':
            return turn, board, True #the True indicates a player quit
        else:
            board[int(play)] = turn

            #Switch current player
            if turn == 'x':
                turn = 'o'
            else:
                turn = 'x'
            
            return turn, board, False

