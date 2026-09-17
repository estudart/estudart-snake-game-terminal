from textual.app import ComposeResult
from textual.widgets import Static, Button, Footer, Header
from textual.containers import Grid

from src.components.time_display import TimeDisplay
from src.components.snake_food import SnakeFood


class GameBoard(Static):
    """Snake Game Board."""

    def __init__(self):
        super().__init__()
        self.game_timer = None
        self.direction = "right"
        self.latest_move = None
        self.width = 60
        self.height = 40
        self.speed = 0.3
        self.body = [[6, 1], [6, 2], [6, 3]]

        self.snake_food = SnakeFood()
        self.food_coordinate = None

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

        self.spawn_food()

        if self.game_timer is None:
            self.game_timer = self.set_interval(
                self.speed,
                self.move_snake
            )

    def spawn_food(self):
        food_coordinate = self.snake_food.get_food_coordinate(
            snake_body=self.body,
            width=self.width-1,
            height=self.height-1,
        )
        food_pixel = self.query_one(
            f"#p{food_coordinate[0]}_{food_coordinate[1]}"
        )
        food_pixel.add_class("snake-food")

        self.food_coordinate = food_coordinate

    def eat_food(self):
        pixel = self.query_one(
            f"#p{self.food_coordinate[0]}_{self.food_coordinate[1]}"
        )
        pixel.remove_class("snake-food")
        self.spawn_food()
        self.game_timer.stop()
        self.speed/=1.2
        self.game_timer._interval = self.speed
        self.game_timer._start()

    def change_direction(self, new_direction: str) -> None:
        if new_direction in ["right", "left", "up", "down"]:
            if self.latest_move == "left" and new_direction == "right":
                return
            if self.latest_move == "right" and new_direction == "left":
                return
            if self.latest_move == "up" and new_direction == "down":
                return
            if self.latest_move == "down" and new_direction == "up":
                return

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

            self.latest_move = "right"

        if self.direction == "left":
            if self.body[-1][1] > 0:
                new_coordinate = [
                    self.body[-1][0],
                    self.body[-1][1] - 1
                ]
            else:
                new_coordinate = [self.body[-1][0], self.width - 1]
            
            self.latest_move = "left"

        if self.direction == "up":
            if self.body[-1][0] > 0:
                new_coordinate = [
                    self.body[-1][0] - 1,
                    self.body[-1][1]
                ]
            else:
                new_coordinate = [self.height - 1, self.body[-1][1]]

            self.latest_move = "up"

        if self.direction == "down":
            if self.body[-1][0] < self.height - 1:
                new_coordinate = [
                    self.body[-1][0] + 1,
                    self.body[-1][1]
                ]
            else:
                new_coordinate = [0, self.body[-1][1]]

            self.latest_move = "down"

        self.body.append(new_coordinate)
        pixel = self.query_one(
            f"#p{new_coordinate[0]}_{new_coordinate[1]}"
        )
        pixel.add_class("cell-deactivate")

        if new_coordinate != self.food_coordinate:
            pixel = self.query_one(
                f"#p{self.body[0][0]}_{self.body[0][1]}"
            )
            pixel.remove_class("cell-deactivate")
            self.body.pop(0)
        else:
            self.eat_food()
