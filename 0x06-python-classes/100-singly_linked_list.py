#!/usr/bin/python3
"""Node of a singly lined list."""


class Node:
    """Defining class Node"""
    def __init__(self, data, next_node=None):
        """Initializing and instance of class Node"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieves data in Class Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets data and if data is not an int it raises an error"""
        self.__data = value

    @property
    def next_node(self):
        """Retrieves next_node in Class Node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets next_node"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defining class SinglyLinkedList"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """A method that inserts a new Node into the correct sorted position in
        the list (increasing order)
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Defining print representation of a SinglyLinkedList"""
        val = []
        temp = self.__head
        while temp is not None:
            val.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(val))
