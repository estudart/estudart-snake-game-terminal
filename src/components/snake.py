import random

class Snake:
    def __init__(
        self,
        body: list[list]
    ) -> None:
        self.body = body

    def is_collision(
        self,
    ) -> bool:
        snake_head = self.body[-1]

        for snake_coordinate in self.body[:-1]:
            if snake_coordinate == snake_head:
                return True
        
        return False
    
    def get_food_coordinate(
        self,
        width: int,
        height: int
    ):
        random_x_coordinate = random.randint(0, width)
        random_y_coordinate = random.randint(0, height)

        food_coordinate = [random_y_coordinate, random_x_coordinate]

        if food_coordinate in self.body:
            self.get_food_coordinate(self.body, width, height)
    
        return food_coordinate
