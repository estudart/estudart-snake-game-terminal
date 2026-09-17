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

        food_coordinate = [random_y_coordinate, random_x_coordinate]

        if food_coordinate in snake_body:
            self.spawn_random(snake_body, width, height)
    
        return food_coordinate
