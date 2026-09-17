from textual.app import ComposeResult
from textual.widgets import Static, Button, Footer, Header
from textual.containers import Grid


class Snake(Static):
    def __init__(self):
        self.size = 10
        
    def compose(self) -> ComposeResult:
        pass
