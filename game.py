class Tic_Tac_Toe:

    def __init__(self):
        self.players = ['Игрок 1', 'Игрок 2']
        self.board = list(range(1, 10))
        self.symbol = ['X', 'O']
        self.move = 0

    def player_names(self):
        for i in range(2):
            print(self.players[i] + ',  представьтесь')
            self.players[i] = input()
            self.check_name(i)
        self.run_game()

    def check_name(self, i):
        while(self.players[i] == ''):
            print('Имя не может быть пустой строкой! Попробуйте ещё раз.')
            self.players[i] = input()

    def one_move(self):
        while self.move <= 4:
            self.move += 1
            for i in range(2):
                print(self.players[i] + ', ваш ход')
                move = self.check_input(input())
                self.board[move - 1] = self.symbol[i]
                self.print_board()
                winner = self.check()
                if winner:
                    return winner
                if self.move == 5:
                    break
        return 0

    def check_input(self, move):
        change = True
        while(change):
            change = False
            while(not move.isdigit() or int(move) <= 0 or int(move) > 9):
                print('Пожалуйста, введите число от 1 до 9!')
                move = input()
                change = True
            while(self.board[int(move) - 1] != int(move)):
                print('Место уже занято! Попробуйте еще раз.')
                move = input()
                change = True
                break
        return int(move)

    def who_win(self, i):
        if self.board[i] == 'X':
            return 1
        return 2

    def check(self):
        if self.move >= 3:
            for i in range(3):
                if self.board[i] == self.board[i + 3] == self.board[i + 6]:
                    return self.who_win(i)
            for i in range(0, 8, 3):
                if self.board[i] == self.board[i + 1] == self.board[i + 2]:
                    return self.who_win(i)
            for i in range(1, 3):
                if self.board[4] == self.board[4 - i * 2] == \
                        self.board[4 + i * 2]:
                    return self.who_win(4)
        return 0

    def print_board(self):
        print('-------------')
        for i in range(9):
            print('| ' + str(self.board[i]) + ' ', end='')
            if (i + 1) % 3 == 0:
                print('|')
                print('-------------')

    def restart(self):
        self.board = list(range(1, 10))
        self.move = 0
        self.players[0], self.players[1] = self.players[1], self.players[0]
        self.run_game()

    def run_game(self):
        self.print_board()
        winner = self.one_move()
        if winner == 1:
            print(self.players[0] + ' победил(а)!')
        elif winner == 2:
            print(self.players[1] + ' победил(а)!')
        else:
            print('Ничья!')
        print('Ещё раз?[д/н]')
        again = input()
        while(again != 'д' and again != 'н'):
            print('Ещё раз?[д/н]')
            again = input()
        if again == 'н':
            return 1
        self.restart()


if __name__ == '__main__':
    Tic_Tac_Toe().player_names()
