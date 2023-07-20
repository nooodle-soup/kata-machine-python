from typing import Optional


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None
