
class Game:
    def __init__(self, player_x, player_o):
        self.player_x = player_x
        self.player_o = player_o
        self.board = [ [" "," "," "], [" "," "," "], [" "," "," "] ]
        self.moves_played = 0
        self.moves_remaining = [1,2,3,4,5,6,7,8,9]
    
    def __get_square(self, row, col):
        return self.board[row][col]
    
    def __set_square(self, row, col, val):
        self.board[row][col] = val
        self.moves_played += 1
    
    def __has_won(self, val):
        won = False
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == val: won = True
        if self.board[1][0] == self.board[1][1] == self.board[1][2] == val: won = True
        if self.board[2][0] == self.board[2][1] == self.board[2][2] == val: won = True
        if self.board[0][0] == self.board[1][0] == self.board[2][0] == val: won = True
        if self.board[0][1] == self.board[1][2] == self.board[2][1] == val: won = True
        if self.board[0][2] == self.board[1][2] == self.board[2][2] == val: won = True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == val: won = True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == val: won = True
        return won
    
    def __draw(self):
        if (not self.__has_won("x")) and (not self.__has_won("o")) and self.moves_played == 9:
            return True
        else:
            return False
    
    @staticmethod
    def get_printable_board(board):
        s = f" {board[0][0]} | {board[0][1]} | {board[0][2]} \n"
        s += "---|---|---\n"
        s += f" {board[1][0]} | {board[1][1]} | {board[1][2]} \n"
        s += "---|---|---\n"
        s += f" {board[2][0]} | {board[2][1]} | {board[2][2]} \n"
        return s

    def play(self):
        turn = "x"
        while (not self.__has_won("x")) and (not self.__has_won("o")) and (not self.__draw()):
            if turn == "x":
                row,col = self.player_x("x", self.board)
                self.__set_square(row, col, "x")
                turn = "o"
            else:
                row,col = self.player_o("o", self.board)
                self.__set_square(row, col, "o")
                turn = "x"
        winner = "-"
        if self.__has_won("x"):
            winner = "x"
        elif self.__has_won("o"):
            winner = "o"
        return winner

def human_prompt(name, board_data):
    print("Current state of the board...")
    print(Game.get_printable_board(board_data))
    print("Player "+name+"...")
    sq = int(input("Enter square number of your move (1=top-left, 9=bottom-right): "))
    sq = sq-1
    row = sq // 3
    col = sq % 3
    return row,col

g = Game(human_prompt,human_prompt)
winner = g.play()
print("The winner was "+winner)

