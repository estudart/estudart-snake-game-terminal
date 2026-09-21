from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Vertical

from src.components.snake_game_board import SnakeGameBoard

class SnakeGame(App):
    CSS_PATH = ["style/game_board.tcss"]

    BINDINGS = [
        ("enter", "start", "Start Game"),
        ("w", "move_up", "Move Up"),
        ("a", "move_left", "Move Left"),
        ("s", "move_down", "Move Down"),
        ("d", "move_right", "Move Right"),
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        
        with Vertical(classes="root"):
            yield Static("Welcome the Game Launcher!")
            yield SnakeGameBoard()
        
        yield Footer()

    def get_board(self) -> SnakeGameBoard:
        return self.query_one(SnakeGameBoard)

    def action_move_up(self):
        self.get_board().change_direction("up")

    def action_move_left(self):
        self.get_board().change_direction("left")

    def action_move_down(self):
        self.get_board().change_direction("down")

    def action_move_right(self):
        self.get_board().change_direction("right")

    def action_start(self):
        board = self.get_board()
        board.start()

if __name__ == "__main__":
    app = SnakeGame()
    app.run()

