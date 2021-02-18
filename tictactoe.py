import random as r
import copy


class TicTacToe:

    def __init__(self):

        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

        self.dict = {1: (0, 0),
                     2: (0, 1),
                     3: (0, 2),
                     4: (1, 0),
                     5: (1, 1),
                     6: (1, 2),
                     7: (2, 0),
                     8: (2, 1),
                     9: (2, 2)
                     }

        self.player = 'X'
        self.computer = 'O'

    def choose(self):
        while True:
            s = input("Would you like to be X or O? ")
            if s.upper() == 'X':
                break
            elif s.upper() == 'O':
                self.player = 'O'
                self.computer = 'X'
                break
            else:
                print('Please pick a valid choice! (X or O)')

    def isFull(self):

        for row in self.board:
            for item in row:
                if item is None:
                    return False

        return True

    def insertMove(self, index, sym, localBoard):

        x = self.dict.get(index)[0]
        y = self.dict.get(index)[1]

        if localBoard[x][y] is None:
            localBoard[x][y] = sym
            return

    def playerTurn(self):

        while True:
            s = int(input("Enter your move (1-9): ").strip())
            if s in self.dict.keys():

                if self.board[self.dict.get(s)[0]][self.dict.get(s)[1]] is None:
                    self.insertMove(s, self.player, self.board)
                    return
                else:
                    print("This cell is full! Enter another move. (1-9)")
            else:
                print('Please pick a valid move. (1-9)')

    def printGame(self, player):
        if player == self.player:
            print('Player: ')
            for row in self.board:
                print(row)
        else:
            print('Computer: ')
            for row in self.board:
                print(row)

    def checkRow(self, localBoard):
        for row in localBoard:
            if len(set(row)) == 1 and set(row).pop() is not None:
                return row[0]
        return -1

    def checkColumn(self, localBoard):
        column = []
        for i in range(len(localBoard)):
            for j in range(len(localBoard[i])):
                column.append(localBoard[j][i])
            if len(set(column)) == 1 and set(column).pop() is not None:
                return column[0]
            column.clear()

        return -1

    def checkDiagonal(self, localBoard):
        if len(set([localBoard[i][i] for i in range(len(localBoard))])) == 1 and set(
                [localBoard[i][i] for i in range(len(localBoard))]).pop() is not None:
            return set([localBoard[i][i] for i in range(len(localBoard))]).pop()
        if len(set([localBoard[i][len(localBoard[i]) - 1 - i] for i in range(len(localBoard))])) == 1 and set(
                [localBoard[i][len(localBoard[i]) - 1 - i] for i in range(len(localBoard))]).pop() is not None:
            return set([localBoard[i][len(localBoard[i]) - 1 - i] for i in range(len(localBoard))]).pop()

        return -1

    def isWinningMove(self, move, sym):
        """checks if a given symbol (x or o) is the winner, returns True if it is """
        localBoard = copy.deepcopy(self.board)
        self.insertMove(move, sym, localBoard)
        if self.checkRow(localBoard) == sym or self.checkColumn(localBoard) == sym \
                or self.checkDiagonal(localBoard) == sym:
            return True
        else:
            return False

    def isWinner(self, sym):

        if self.checkRow(self.board) == sym or self.checkColumn(self.board) == sym or self.checkDiagonal(
                self.board) == sym:
            return True
        else:
            return False

    def isEmptyCell(self, move):
        x = self.dict.get(move)[0]
        y = self.dict.get(move)[1]

        if self.board[x][y] is None:
            return True

        return False

    def computerTurn(self):
        for i in range(1, 10):
            if self.isWinningMove(i, self.computer):
                self.insertMove(i, self.computer, self.board)
                return

        for i in range(1, 10):
            if self.isWinningMove(i, self.player):
                self.insertMove(i, self.computer, self.board)
                return

        if self.isEmptyCell(5):
            self.insertMove(5, self.computer, self.board)
            return

        for i in range(4):
            rand = r.choice([1, 3, 7, 9])
            if self.isEmptyCell(rand):
                self.insertMove(rand, self.computer, self.board)
                return

        for i in range(4):
            rand = r.choice([2, 4, 6, 8])
            if self.isEmptyCell(rand):
                self.insertMove(rand, self.computer, self.board)
                return

    def mainloop(self):
        self.choose()
        ch = r.randint(0, 1)
        if ch == 1:
            print("Player goes first!")
            while True:

                self.playerTurn()
                self.printGame(self.player)
                if self.isWinner(self.player):
                    print('Player wins!')
                    break

                if self.isFull():
                    print("Game drawn!")
                    break
                self.computerTurn()
                self.printGame(self.computer)
                if self.isWinner(self.computer):
                    print('Computer wins!')
                    break

                if self.isFull():
                    print("Game drawn!")
                    break


        else:

            print("Computer goes first!")
            while True:
                self.computerTurn()
                self.printGame(self.computer)
                if self.isWinner(self.computer):
                    print("Computer wins!")
                    break

                if self.isFull():
                    print("Game drawn!")
                    break

                self.playerTurn()
                self.printGame(self.player)
                if self.isWinner(self.player):
                    print("Player wins!")
                    break

                if self.isFull():
                    print("Game drawn!")
                    break


if __name__ == '__main__':
    game = TicTacToe()
    while True:
        game1 = TicTacToe()
        game1.mainloop()
        choice = input("Do you want to play again? [y/N] ")
        if choice.upper() == 'N':
            break

    print("Thank you for playing!")
