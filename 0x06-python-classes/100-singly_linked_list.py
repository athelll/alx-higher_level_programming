#!/usr/bin/python3
"""

Module: 100-singly_linked_list
creates a singly list data strucrure
With ascending sorting algorithm

"""


class Node:
    """
    Node Class of singly list
    """
    def __init__(self, data, next_node=None):
        """
        Initialization function

            Args: data, next_node
        """
        self.data = data
        self.nxnode = next_node

    # set the getter for data
    @property
    def data(self):
        """
        getter function of data property
        """
        return self.__data

    # set the setter for data must be integer
    @data.setter
    def data(self, value):
        """
        Setter function for data property
            Args: value
        """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    # set the getter for next_node
    @property
    def next_node(self):
        """
        getter function for next node
        """
        return self.__nxnode

    # set the setter for next_node can be none or of type Node
    @next_node.setter
    def next_node(self, value):
        """
        setter for next node
            Args: value
        """
        if type(value) is not Node or type(value) is not None:
            raise TypeError('next_node must be a Node object')
        else:
            self.__nxnode = value


class SinglyLinkedList:
    """
    SinglyLinkedList Class
    """
    def __init__(self):
        """
        Initialization function
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        function for inserting nodes in
        singlylinkedlist
            Args: self, value
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        tmp = self.__head
        if new.data < tmp.data:
            new.nxnode = self.__head
            self.__head = new
            return

        while(tmp.nxnode is not None) and (new.data > tmp.nxnode.data):
            tmp = tmp.nxnode
        new.nxnode = tmp.nxnode
        tmp.nxnode = new
        return

    def __str__(self):
        """
        Handles the print() function on this
        class instances
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.nxnode
            if tmp is not None:
                string += '\n'
        return string
