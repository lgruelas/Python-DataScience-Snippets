from linked_list import LinkedList

class HashTable:
    '''
        Hash table implementation using separate chaining for hash collition
    '''
    def __init__(self, array_size=10):
        self._array_size = array_size
        self._array = [LinkedList() for _ in range(array_size)]

    def __hash(self, key):
        key_bytes = key.encode()
        return sum(key_bytes)
    
    def __compressor(self, hash_value):
        return hash_value % self._array_size

    def assign(self, key, value):
        index = self.__compressor(self.__hash(key))
        linked_list = self._array[index]
        if linked_list.is_empty():
            linked_list.append([key, value])
        else:
            for node_value in linked_list:
                if node_value[0] == key:
                    node_value[1] = value
                    return        
            linked_list.append([key, value])
    
    def retrieve(self, key):
        index = self.__compressor(self.__hash(key))
        linked_list = self._array[index]
        for node_value in linked_list:
            if node_value[0] == key:
                return node_value[1]
