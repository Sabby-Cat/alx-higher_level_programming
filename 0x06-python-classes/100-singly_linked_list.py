#!/usr/bin/python3
"""Define class singly-linked list and nod"""


class Node:
    """Represent node in singly-linked list."""
    def __init__(self, data, next_node=None):
        """Initialize new Node.
        Args:
            data (int): data of new Node.
            next_node (Node): next node of new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set data of Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Get/set next_node of Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Represent singly-linked list."""
    def __init__(self):
        """Initalize new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new Node in SinglyLinkedList.
        node is inserted into list at correct
        ord num position.
        Args:
            value (Node): new Node to insert.
        """
        node = self.__head
        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)

    def __str__(self):
        """Define print() rep of SinglyLinkedList."""
        ret = ""
        node = self.__head
        while node is not None:
            ret += str(node.data) + '\n'
            node = node.next_node
        return ret[:-1]
