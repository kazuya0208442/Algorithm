from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, data: Any, next_node: Node = None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        

if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.insert(0)
    print(l.head.data)
    print(l.head.next.data)
    print(l.head.next.next.data)
    print(l.head.next.next.next.data)