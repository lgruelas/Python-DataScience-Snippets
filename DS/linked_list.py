#! /usr/bin/python3

#DATA STRUCTURES FOR PYTHON3

class LinkedList:
    class __Node:
        def __init__(self, value, next_node=None):
            self._value = value
            self._next_node = next_node
        
        def get_value(self):
            return self._value
        
        def get_next_node(self):
            return self._next_node

        def set_next_node(self, new_node):
            self._next_node = new_node

    def __init__(self):
        self._num_elements = 0
        self._head_node = LinkedList.__Node(None)

    def __getitem__(self, index):
        if index >= 0 and index < self._num_elements:
            current_node = self._head_node.get_next_node()
            for _ in range(index):
                current_node = current_node.get_next_node()
            return current_node.get_value()
        raise IndexError("LinkedList index out of range")

    def is_empty(self):
        return self._num_elements == 0

    def get_head_value(self):
        if not self.is_empty:
            return self._head_node.get_next_node().get_value()
        return None
    
    def insert_beggining(self, new_value):
        new_node = LinkedList.__Node(new_value, self._head_node.get_next_node())
        self._head_node.set_next_node(new_node)
        self._num_elements += 1

    def append(self, value):
        new_node = LinkedList.__Node(value)
        current_node = self._head_node
        while current_node.get_next_node():
            current_node = current_node.get_next_node()
        current_node.set_next_node(new_node)
        self._num_elements += 1 
        
    def insert(self, value, index):
        new_node = LinkedList.__Node(value)
        if index >= 0 and index < self._num_elements:
            current_node = self._head_node
            for _ in range(index):
                current_node = current_node.get_next_node()
            new_node.set_next_node(current_node.get_next_node())
            current_node.set_next_node(new_node)
            self._num_elements += 1 
        else:
            raise IndexError("LinkedList index out of range")

    def remove_by_index(self, index):
        if index >= 0 and index < self._num_elements:
            current_node = self._head_node
            for _ in range(index):
                current_node = current_node.get_next_node()
            current_node.set_next_node(current_node.get_next_node().get_next_node())
            self._num_elements -= 1
        else:
            raise IndexError("LinkedList index out of range")

    def remove_by_value(self, value_to_remove):
        '''
            Removes the first Node that the value is equal to the parameter passed.
        '''
        current_node = self._head_node
        while current_node:
            if current_node.get_next_node().get_value() == value_to_remove:
                current_node.set_next_node(current_node.get_next_node().get_next_node())
                self._num_elements -= 1
                break
            current_node = current_node.get_next_node()
        
    def to_string(self):
        values_list = []
        current_node = self._head_node.get_next_node()
        while current_node:
            values_list.append(current_node.get_value())
            current_node = current_node.get_next_node()
        return "->".join(map(str, values_list))
