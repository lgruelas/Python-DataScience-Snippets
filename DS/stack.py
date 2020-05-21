#! /usr/bin/python3

#DATA STRUCTURES FOR PYTHON3

from node import Node
from exceptions import FlowException

class Stack:
    def __init__(self, limit=100):
        self._top_item = None
        self._size = 0
        self._limit = limit

    def push(self, value):
        if not self.__has_space():
            raise FlowException("OverFlow error, the stack is full")
        new_node = Node(value, self._top_item)
        self._size += 1
        self._top_item = new_node

    def pop(self):
        if self.__is_empty():
            raise FlowException("UnderFlow error, the stack is empty")
        to_return = self._top_item.get_value()
        self._top_item = self._top_item.get_next_node()
        self._size -= 1
        return to_return
    
    def peek(self):
        if self.__is_empty():
            raise FlowException("UnderFlow error, the stack is empty")
        return self._top_item.get_value()

    def __has_space(self):
        return self._limit > self._size

    def __is_empty(self):
        return self._size == 0