from src.katas.Queue import Queue
from src.katas.Node import Node
import pytest


@pytest.mark.queue
def test_queue():
    x = Queue()
    x.enqueue(Node(1))
    x.enqueue(Node(2))

    assert x.length == 2

    assert x.dequeue().value == 1

    x.dequeue()
    assert x.length == 0
