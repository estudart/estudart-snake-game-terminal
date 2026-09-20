from src.components.snake import Snake

def test_snake_collision_returns_true():
    snake_body = [[1, 1], [1, 2], [2, 2], [2, 1], [1, 1]]
    snake = Snake(body=snake_body)
    is_collision = snake.is_collision()
    assert is_collision

def test_snake_collision_returns_false():
    snake_body = [[1, 1], [1, 2], [2, 2], [2, 1]]
    snake = Snake(body=snake_body)
    is_collision = snake.is_collision()
    assert not is_collision
