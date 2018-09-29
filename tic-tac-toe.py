from random import randint
from time import sleep

class TicTacToe:
    def __init__(self):
        self.__pieces  = [['*']*3 for i in range(3)]
        self.player_piece = ['O', 'X'] # computer plays 'O', you play 'X'
        print('\n%20s' % '----tic-tac-toe----')
        self.print_board()
        self.turn = int(input('who moves first? 0: computer (%s), 1: you (%s):  ' %
                          (self.player_piece[0], self.player_piece[1]) ) )
        self.tie = False
        self.computer_win = False
        self.player_win = False 
        
    def print_board(self):
        print('\n')
        for r in range(3):
            for c in range(3):
                print('%5s' % self.__pieces[r][c], end='')
            print('\n')

    def start(self):
        while (not self.tie and not self.computer_win and not self.player_win):
            if (self.turn == 0):  # computer move, just randomly
                print('computer move')
                sleep(2)
                r, c = self.get_rc()
                self.move(r, c)
                self.turn = 1 
            else: # player's turn
                quit = input('now your turn, type <q> to quit, any key to continue:  ')
                if(quit == 'q'):
                    break
                print('\nmove to:') 
                r = int(input('row (1, 2 or 3): ')) -1
                c = int(input('column (1, 2 or 3): ')) -1
                if (self.move(r, c)):
                    self.turn = 0  
                else:
                    self.turn = 1
        if (self.tie):
            print('tie reached, game over')
        if (self.computer_win):
            print('computer win, game over :(')
        if (self.player_win):
            print('you win, congratulations!')
                    

    # defines how computer moves
    def get_rc(self):
        empty = []
        for r in range(3):
            for c in range(3):
                if self.can_move(r, c):
                    empty.append([r, c])
        if len(empty) == 0:
            return None
        select = randint(0, len(empty) - 1)
        return empty[select]


    def check_tie(self):
        if not self.get_rc():
            self.tie = True


    def check_win(self, row, col):
        if ( len(set(self.__pieces[row])) == 1 or # same elements in row
             len(set([row[col] for row in self.__pieces])) == 1 or # same lements in column
             (row == col and len(set([self.__pieces[r][r] for r in range(3)])) == 1) or # same elements in diagonal
             (row == (2-col) and len(set([self.__pieces[r][2-r] for r in range(3)])) == 1) ): # same elements in contra diagonal
            if (self.turn == 0):
                self.computer_win  = True
            if(self.turn == 1):
                self.player_win = True

          
                                     
    def move(self, row, col):
        if self.can_move(row, col):
            self.__pieces[row][col] = self.player_piece[self.turn]
            self.check_tie()
            self.check_win(row, col)
            success = True
        else:
            print('cannot move to (row = %d, column = %d), try again' % (row + 1, col + 1))
            success = False
        self.print_board()
        return success
        

    def can_move(self, row, col):
        return (self.__pieces[row][col] == '*')

game = TicTacToe()
game.start()