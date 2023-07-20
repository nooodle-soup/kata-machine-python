from src.katas.Node import Node
from typing import Optional, Any


class Stack:
    def __init__(self) -> None:
        self.length = 0
        self.head: Optional[Node] = None

    def push(self, value: Any) -> bool:
        node = Node(value)
        if self.length == 0:
            self.head = node
        else:
            assert self.head is not None
            self.head.next = node
            self.head = node
        self.length += 1
        return True

    def pop(self) -> object:
        if self.length > 0:
            assert self.head is not None
            head = self.head
            self.head = head.prev
            self.length -= 1
            return head.value
        return None

    def peek(self) -> object:
        if self.length > 0:
            assert self.head is not None
            return self.head.value
        return None
                    
