from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

from src.components.game_board import GameBoard

class SnakeGame(App):
    CSS_PATH = ["components/game_board.tcss"]

    BINDINGS = [
        ("enter", "start", "Start Game"),
        ("w", "move_up", "Move Up"),
        ("a", "move_left", "Move Left"),
        ("s", "move_down", "Move Down"),
        ("d", "move_right", "Move Right"),
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("Welcome to the Python Snake Game!")
        yield GameBoard()
        yield Footer()

    def get_board(self) -> GameBoard:
        return self.query_one(GameBoard)

    def action_start(self):
        board = self.get_board()
        board.start()

if __name__ == "__main__":
    app = SnakeGame()
    app.run()

