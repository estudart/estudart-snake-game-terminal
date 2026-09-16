from textual.app import ComposeResult
from textual.widgets import Static, Button, Footer, Header
from textual.containers import Grid

from src.components.time_display import TimeDisplay


class GameBoard(Static):
    """Snake Game Board."""

    def __init__(self):
        super().__init__()
        self.game_timer = None

    def compose(self) -> ComposeResult:
        yield TimeDisplay("00:00:00.00", id="time-display")

        with Grid(id="board-grid"):
            for row in range(20):
                for col in range(60):
                    yield Static(
                        f"+", 
                        id=f"p{row}_{col}", 
                        classes="cell"
                    )

    def on_mount(self) -> None:
        self.focus()

    def move_snake(self):
        pass

    def start(self):
        pixel = self.query_one("#p1_1")
        pixel.add_class("cell-deactivate")
        if self.game_timer is None:
            self.game_timer = self.set_interval(
                0.5,
                self.move_snake
            )

