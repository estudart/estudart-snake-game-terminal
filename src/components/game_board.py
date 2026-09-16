from textual.app import ComposeResult
from textual.widgets import Static, Button, Footer, Header
from textual.containers import Grid

from src.components.time_display import TimeDisplay


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


class GameBoard(Static):
    """Snake Game Board."""

    def __init__(self):
        super().__init__()
        self.game_timer = None
        self.direction = "right"
        self.width = 60
        self.height = 20
        self.speed = 0.3
        self.body = LinkedList([6, 1])
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
        temp = self.body.head
        while temp is not None:
            pixel = self.query_one(
                f"#p{temp.value[0]}_{temp.value[1]}"
            )
            pixel.add_class("cell-deactivate")
            temp = temp.next

        if self.game_timer is None:
            self.game_timer = self.set_interval(
                self.speed,
                self.move_snake
            )

    def move_snake(self):
        if self.direction == "right":
            if self.body.tail.value[1] < self.width - 1:
                new_coordinate = [
                    self.body.tail.value[0],
                    self.body.tail.value[1]+1
                ]
            else:
                new_coordinate = [self.body.tail.value[0], 0]

            self.body.append(new_coordinate)
            pixel = self.query_one(
                f"#p{new_coordinate[0]}_{new_coordinate[1]}"
            )
            pixel.add_class("cell-deactivate")

            pixel = self.query_one(
                f"#p{self.body.head.value[0]}_{self.body.head.value[1]}"
            )
            pixel.remove_class("cell-deactivate")
            self.body.pop_first()


            
