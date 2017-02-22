import sys


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    def hasTwoItems(self):
        if len(self.items) >= 2:
            return True
        else:
            return False

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

    def size(self):
        return len(self.items)

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

