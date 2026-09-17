import random

from textual.widgets import Static


class SnakeFood(Static):
    def get_food_coordinate(
        self,
        snake_body: list[list],
        width: int,
        height: int
    ):
        random_x_coordinate = random.randint(0, width)
        random_y_coordinate = random.randint(0, height)
    
        return [random_y_coordinate, random_x_coordinate]
