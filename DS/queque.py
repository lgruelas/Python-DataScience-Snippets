#! /usr/bin/python3

#DATA STRUCTURES FOR PYTHON3

from node import Node
from exceptions import FlowException


class Queue:
    def __init__(self, limit=None):
        self._head_node = None
        self._tail_node = None
        self._limit = limit
        self._size = 0

    def peek(self):
        if self.__is_empty():
            raise FlowException("UnderFlow Error, the queue is empty")
        return self._tail_node.get_value()

    def enqueue(self, value):
        if not self.__has_space():
            raise FlowException("OverFLow Error, the queue is already full")
        new_node = Node(value)
        if self.__is_empty():
            self._head_node = new_node
            self._tail_node = new_node
        else:
            self._tail_node.set_next_node(new_node)
            self._tail_node = new_node
        self._size += 1

    def dequeue(self):
        if self.__is_empty():
            raise FlowException("UnderFlow Error, the queue is empty")
        to_return = self._head_node.get_value()
        if self._size == 1:
            self._head_node = None
            self._tail_node = None
        else:
            self._head_node = self._head_node.get_next_node()
        self._size -= 1
        return to_return

    def __has_space(self):
        if self._limit:
            return self._size < self._limit
        return True

    def __is_empty(self):
        return self._size == 0
