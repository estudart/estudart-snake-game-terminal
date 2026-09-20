

class Snake:
    def is_collision(
        self,
        snake_body: list[list]
    ) -> bool:
        snake_head = snake_body[-1]

        for snake_coordinate in snake_body[:-1]:
            if snake_coordinate == snake_head:
                return True
        
        return False
