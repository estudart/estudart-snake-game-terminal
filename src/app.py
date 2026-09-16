from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

from src.components.game_board import GameBoard

class SnakeGame(App):
    CSS_PATH = ["components/game_board.tcss"]

    BINDINGS = [("d", "change_mode", "Switch to dark mode")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("Welcome to the Python Snake Game!")
        yield GameBoard()
        yield Footer()

    def action_change_mode(self):
        pass

if __name__ == "__main__":
    app = SnakeGame()
    app.run()

