#! /usr/bin/python3

#DATA STRUCTURES FOR PYTHON3

class Node:
    def __init__(self, value, next_node=None):
        self._value = value
        self._next_node = next_node
    
    def get_value(self):
        return self._value
    
    def get_next_node(self):
        return self._next_node

    def set_next_node(self, new_node):
        self._next_node = new_node

    def __repr__(self):
        if self.get_next_node():
            return "{}->{}".format(self.get_value(), self.get_next_node().get_value())
        else:
            return str(self.get_value())