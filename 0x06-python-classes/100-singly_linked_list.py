#!/usr/bin/python3
"""This module creates a singly linked list
"""


class Node:
    """Class to add node to linked list
    """
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    """Singly linked list class
    """
    def __init__(self):
        self.__head = None

    def __repr__(self):
        ptr = self.__head
        txt = ''
        while ptr:
            txt += str(ptr.data)
            if ptr.next_node is None:
                break
            else:
                txt += '\n'
            ptr = ptr.next_node
        return txt

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            hld = None
            ptr = self.__head
            while ptr:
                if ptr.data > value:
                    new = Node(value, ptr)
                    if ptr is self.__head:
                        self.__head = new
                    else:
                        hld.next_node = new
                    break

                hld = ptr
                ptr = ptr.next_node

            if not ptr:
                new = Node(value)
                hld.next_node = new
