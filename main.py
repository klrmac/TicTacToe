import tkinter as tk
from game_board import GameBoard

def main():
    # Creating the root window
    root = tk.Tk()
    root.title('Tic-Tac-Toe')

    # Setting window size
    root.geometry('400x450')  # Adjusted window size to accommodate control interface

    # Frame for the game board
    game_board_frame = tk.Frame(root)
    game_board_frame.pack()

    # Initialize the game board
    game_board = GameBoard(game_board_frame)
    print("Game board initialized.")

    # Game status label
    status_label = tk.Label(root, text="Player X's turn", font=('Arial', 14))
    status_label.pack(pady=20)

    # Frame for game mode selection and control buttons
    control_frame = tk.Frame(root)
    control_frame.pack(pady=20)

    # Game mode selection buttons
    single_player_btn = tk.Button(control_frame, text="Single Player", font=('Arial', 12), command=lambda: select_game_mode('single'))
    single_player_btn.grid(row=0, column=0, padx=10)

    two_player_btn = tk.Button(control_frame, text="Two Player", font=('Arial', 12), command=lambda: select_game_mode('two'))
    two_player_btn.grid(row=0, column=1, padx=10)

    # Play again and quit buttons
    # play_again_btn = tk.Button(root, text="Play Again", font=('Arial', 12), command=play_again)
    # play_again_btn.pack(pady=5)

    quit_btn = tk.Button(root, text="Quit", font=('Arial', 12), command=root.quit)
    quit_btn.pack(pady=5)

    # Implement select_game_mode function
    def select_game_mode(mode):
        print(f"Game mode selected: {mode}")
        # Placeholder for functionality to switch game modes
        # This will be fully implemented in a later task

    # Implement play_again function
    def play_again():
        print("Resetting the game...")
        # Placeholder for functionality to reset the game
        # This will be fully implemented in a later task

    # Gracefully handle window closure
    def on_close():
        print("Closing application")
        root.quit()

    root.protocol("WM_DELETE_WINDOW", on_close)

    # Start the GUI event loop
    try:
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
        print(e.__traceback__)

if __name__ == "__main__":
    main()