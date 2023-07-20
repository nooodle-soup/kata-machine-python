from src.katas.Node import Node
from typing import Optional, Any


class Queue:
    def __init__(self) -> None:
        self.length = 0
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def enqueue(self, value: Any) -> bool:
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            assert self.tail is not None
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def dequeue(self) -> object:
        if self.length > 0:
            assert self.head is not None
            head = self.head
            self.head = head.next
            head.next = None
            self.length -= 1
            return head.value
        return None

    def peek(self) -> object:
        if self.length > 0:
            assert self.head is not None
            return self.head.value
        return None

