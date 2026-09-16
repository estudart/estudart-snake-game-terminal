from textual.app import ComposeResult
from textual.widgets import Static, Button, Footer, Header
from textual.containers import Grid

from src.components.time_display import TimeDisplay


class GameBoard(Static):
    """Snake Game Board."""

    def __init__(self):
        super().__init__()
        self.game_timer = None
        self.direction = "right"
        self.prev_direction = None
        self.width = 60
        self.height = 20
        self.speed = 0.3
        self.body = [[6, 1]]
        self.body.append([6, 2])
        self.body.append([6, 3])

    def compose(self) -> ComposeResult:
        yield TimeDisplay("00:00:00.00", id="time-display")

        with Grid(id="board-grid"):
            for row in range(self.height):
                for col in range(self.width):
                    yield Static(
                        f"", 
                        id=f"p{row}_{col}", 
                        classes="cell"
                    )

    def start(self):
        for coordinate in self.body:
            pixel = self.query_one(
                f"#p{coordinate[0]}_{coordinate[1]}"
            )
            pixel.add_class("cell-deactivate")

        if self.game_timer is None:
            self.game_timer = self.set_interval(
                self.speed,
                self.move_snake
            )

    def change_direction(self, new_direction: str) -> None:
        if new_direction in ["right", "left", "up", "down"]:
            if self.direction == "left" and new_direction == "right":
                return
            if self.direction == "right" and new_direction == "left":
                return
            if self.direction == "up" and new_direction == "down":
                return
            if self.direction == "down" and new_direction == "up":
                return
            self.prev_direction = self.direction
            self.direction = new_direction

    def move_snake(self):
        if self.direction == "right":
            if self.body[-1][1] < self.width - 1:
                new_coordinate = [
                    self.body[-1][0],
                    self.body[-1][1]+1
                ]
            else:
                new_coordinate = [self.body[-1][0], 0]

            self.body.append(new_coordinate)
            pixel = self.query_one(
                f"#p{new_coordinate[0]}_{new_coordinate[1]}"
            )
            pixel.add_class("cell-deactivate")

            pixel = self.query_one(
                f"#p{self.body[0][0]}_{self.body[0][1]}"
            )
            pixel.remove_class("cell-deactivate")
            self.body.pop(0)

        if self.direction == "left":
            if self.body[-1][1] > 0:
                new_coordinate = [
                    self.body[-1][0],
                    self.body[-1][1] - 1
                ]
            else:
                new_coordinate = [self.body[-1][0], self.width - 1]

            self.body.append(new_coordinate)
            pixel = self.query_one(
                f"#p{new_coordinate[0]}_{new_coordinate[1]}"
            )
            pixel.add_class("cell-deactivate")

            pixel = self.query_one(
                f"#p{self.body[0][0]}_{self.body[0][1]}"
            )
            pixel.remove_class("cell-deactivate")
            self.body.pop(0)

        if self.direction == "down":
            if self.body[-1][0] < self.height - 1:
                new_coordinate = [
                    self.body[-1][0] + 1,
                    self.body[-1][1]
                ]
            else:
                new_coordinate = [0, self.body[-1][1]]

            self.body.append(new_coordinate)
            pixel = self.query_one(
                f"#p{new_coordinate[0]}_{new_coordinate[1]}"
            )
            pixel.add_class("cell-deactivate")

            pixel = self.query_one(
                f"#p{self.body[0][0]}_{self.body[0][1]}"
            )
            pixel.remove_class("cell-deactivate")
            self.body.pop(0)

        if self.direction == "up":
            if self.body[-1][0] > 0:
                new_coordinate = [
                    self.body[-1][0] - 1,
                    self.body[-1][1]
                ]
            else:
                new_coordinate = [self.height - 1, self.body[-1][1]]

            self.body.append(new_coordinate)
            pixel = self.query_one(
                f"#p{new_coordinate[0]}_{new_coordinate[1]}"
            )
            pixel.add_class("cell-deactivate")

            pixel = self.query_one(
                f"#p{self.body[0][0]}_{self.body[0][1]}"
            )
            pixel.remove_class("cell-deactivate")
            self.body.pop(0)
