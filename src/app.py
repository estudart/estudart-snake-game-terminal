from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class MyPanel(App):
    BINDINGS = [("d", "change_mode", "Switch to dark mode")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("Welcome to the Python Snake Game!")
        yield Footer()

if __name__ == "__main__":
    app = MyPanel()
    app.run()

