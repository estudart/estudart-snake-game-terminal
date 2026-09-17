from textual.widgets import Static


class Score(Static):
    def __init__(self):
        self.value = 0

    def add(self) -> None:
        self.value+=1
