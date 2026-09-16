from textual.app import ComposeResult
from textual.widgets import Static, Button, Footer, Header
from textual.containers import Grid

from src.components.time_display import TimeDisplay


class GameBoard(Static):
    """Snake Game Board."""

    def compose(self) -> ComposeResult:
        yield TimeDisplay("00:00:00.00", id="time-display")
        with Grid(id="board-grid"):
            for row in range(20):
                for col in range(60):
                    if col == 5 and row == 1:
                        yield Static(f"+", classes="test-cell")
                    if col == 4 and row == 1:
                        yield Static(f"+", classes="test-cell")
                    else:
                        yield Static(f"+++", classes="cell")

