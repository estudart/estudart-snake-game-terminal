from src.components.snake import Snake

def test_snake_collision_returns_true():
    snake_body = [[1, 1], [1, 2], [2, 2], [2, 1], [1, 1]]
    is_collision = Snake().is_collision(snake_body=snake_body)

    assert is_collision

def test_snake_collision_returns_false():
    snake_body = [[1, 1], [1, 2], [2, 2], [2, 1]]
    is_collision = Snake().is_collision(snake_body=snake_body)

    assert not is_collision
