class Node:
    '''This is a class denoting a Node'''
    def __init__(self, data, next_node=None):
        '''This is the initialiser method'''
        self.data = data
        self.next_node = next_node

    @property
    ''' retrieving the value private value of data '''
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    ''' retrieving the value private value of next_node '''
    def next_node(self):
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if isinstance(value, int):
            self.__next_node = value
        elif value == None:
            self.__next_node = None
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    '''This is a class denoting a singly linked list'''
    def __init__(self, head):
        self.__head = head
        
