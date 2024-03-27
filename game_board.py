import tkinter as tk
from tkinter import messagebox

class GameBoard:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.board_state = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.initialize_board()

    def initialize_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.parent_frame, text='', font=('Arial', 20), height=3, width=6,
                                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                self.buttons[row][col].grid(row=row, column=col)
                print(f"Button for cell [{row}][{col}] initialized.")

    def on_button_click(self, row, col):
        if self.board_state[row][col] == '' and self.current_player:
            self.buttons[row][col].config(text=self.current_player)
            self.board_state[row][col] = self.current_player
            print(f"Cell [{row}][{col}] marked with '{self.current_player}'.")
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            print(f"It's now {self.current_player}'s turn.")
            if self.check_win_condition():
                self.disable_all_buttons()
        else:
            print(f"Cell [{row}][{col}] is already marked. Please choose another cell.")

    def check_win_condition(self):
        # Check rows, columns, and diagonals for a win condition
        for i in range(3):
            if self.board_state[i][0] == self.board_state[i][1] == self.board_state[i][2] != '':
                messagebox.showinfo("Game Over", f"Player {self.board_state[i][0]} wins by row {i}!")
                return True
            if self.board_state[0][i] == self.board_state[1][i] == self.board_state[2][i] != '':
                messagebox.showinfo("Game Over", f"Player {self.board_state[0][i]} wins by column {i}!")
                return True
        if self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2] != '' or \
           self.board_state[0][2] == self.board_state[1][1] == self.board_state[2][0] != '':
            messagebox.showinfo("Game Over", "Player wins diagonally!")
            return True
        if all(self.board_state[row][col] != '' for row in range(3) for col in range(3)):
            messagebox.showinfo("Game Over", "The game is a draw.")
            return True
        return False

    def disable_all_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state='disabled')