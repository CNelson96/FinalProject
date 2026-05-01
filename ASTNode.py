# I certify that the Python file I am submitting is all my own work.
# None of it is copied from any source or any person.
# Signed: Cory Nelson, Marcus Her, Nou Chai Thao.
# Date: 5/01/2026
#
# Author: Cory Nelson, Marcus Her, Nou Chai Thao.
# Date:  5/01/2026
# Class: CSS335
# Assignment: Final Project Banking
# File Name: ASTNode.py
# Description: Creating the AST for the banking program
#







# Represents one node in the AST. Nodes can have child nodes
# to represent compound commands like CREATE_ACCOUNT.
class ASTNode:

    # node_type: label for this node (e.g. "DEPOSIT")
    # children:  list of child ASTNodes (empty by default)
    # value:     optional data like an amount or name string
    def __init__(self, node_type, children=None, value=None):
        self.__node_type = node_type
        self.__children  = children if children is not None else []
        self.__value     = value

    # Getters

    def get_node_type(self):
        return self.__node_type

    def get_children(self):
        return self.__children

    def get_value(self):
        return self.__value

    # Print the full tree with indentation when this node is displayed
    def __repr__(self):
        return self.__build_repr(indent=0)

    # Recursive helper builds the indented string for this node
    # and all its children
    def __build_repr(self, indent):
        prefix = "  " * indent

        # Include value in the line only if one exists
        if self.__value is not None:
            line = f"{prefix}ASTNode({self.__node_type}, value={self.__value})"
        else:
            line = f"{prefix}ASTNode({self.__node_type})"

        # Recurse into each child with one extra level of indent
        child_lines = []
        index = 0
        while index < len(self.__children):
            child_lines.append(self.__children[index].__build_repr(indent + 1))
            index += 1

        if len(child_lines) > 0:
            result = line + "\n" + "\n".join(child_lines)
        else:
            result = line

        return result
