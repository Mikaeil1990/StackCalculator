
import sys


class Stack:
    """This is Stack class holds all the functionalities of a stack:
    variables:
    items:  A list which holds numbers in the stack

    functions:
    isEmpty(): returns True if Stack is empty.
    hasTwoItems(): returns True if there are more than 2 numbers in stack.
    size(): return the size of stack.
    push(): pushes 1 number to the stack.
    pop(): delete and return the top of stack.
    peek(): return the to of stack.
    add(): return the result of adding the top 2 values in stack.
    sub(): return the result of subtracting the top 2 values in stack.
    mul(): return the result of multiplying the top 2 values in stack.
    div(): return the result of division of top 2 values in stack.

    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def hasTwoItems(self):
        if len(self.items) >= 2:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

    def push(self, item):
        try:
            self.items.append(item)
            print self.items
            return "{} Added!".format(item)
        except:
            e = sys.exc_info()[0]
        return str(e)


    def pop(self):
        try:
            return self.items.pop()
        except Exception as e:
            return e

    def peek(self):
        return self.items[len(self.items) - 1]


    def add(self):
        top = self.items.pop()
        toplast = self.items.pop()
        add = top + toplast
        self.items.append(add)
        return self.items[len(self.items) - 1]

    def sub(self):
        top = self.items.pop()
        toplast = self.items.pop()
        sub = toplast - top
        self.items.append(sub)
        return self.items[len(self.items) - 1]

    def mul(self):
        top = self.items.pop()
        toplast = self.items.pop()
        mul = toplast * top
        self.items.append(mul)
        return self.items[len(self.items) - 1]

    def div(self):
        try:
            top = self.items.pop()
            toplast = self.items.pop()
            div = toplast / top
            self.items.append(div)
            return self.items[len(self.items) - 1]
        except Exception as e:
            self.items.append(toplast)
            self.items.append(top)
            return e

