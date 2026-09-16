from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class MeuPainel(App):
    BINDINGS = [("d", "mudar_modo", "Alternar Modo Escuro")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("Bem-vindo à TUI gerada com Python e Textual!")
        yield Footer()

if __name__ == "__main__":
    app = MyPanel()
    app.run()

