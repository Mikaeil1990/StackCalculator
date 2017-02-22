from flask import Flask, render_template
from Model.Stack import Stack

app = Flask(__name__)
app.config.from_pyfile('app.cfg')

StacksHolder = {}

def checkRequest(id):
    flag_stackExist = False
    for key, value in StacksHolder.iteritems():
        if key == id:
            flag_stackExist = True
    if flag_stackExist == False:
        StacksHolder[id] = Stack()


@app.route("/")
def index():
    return str(StacksHolder)

@app.route('/calc/<int:id>/peek')
def peek(id):
    checkRequest(id)
    if StacksHolder[id].isEmpty():
        return "Stack is Empty."
    return str(StacksHolder[id].peek())
    # xx = str(id)
    # return str(StacksHolder)

@app.route("/calc/<int:id>/push/<int:n>")
def push(id, n):
    checkRequest(id)
    res = StacksHolder[id].push(n)
    return res

@app.route('/calc/<int:id>/pop')
def pop(id):
    checkRequest(id)
    if StacksHolder[id].isEmpty():
        return "Stack is Empty."
    return str(StacksHolder[id].pop())
    # xx = str(id)
    # return str(StacksHolder)

@app.route('/calc/<int:id>/add')
def add(id):
    checkRequest(id)
    if StacksHolder[id].hasTwoItems():
        return str(StacksHolder[id].add())
    return "Stack has less than 2 items."
    # xx = str(id)
    # return str(StacksHolder)

@app.route('/calc/<int:id>/subtract')
def sub(id):
    checkRequest(id)
    if StacksHolder[id].hasTwoItems():
        return str(StacksHolder[id].sub())
    return "Stack has less than 2 items."
    # xx = str(id)
    # return str(StacksHolder)
@app.route('/calc/<int:id>/multiply')
def mul(id):
    checkRequest(id)
    if StacksHolder[id].hasTwoItems():
        return str(StacksHolder[id].mul())
    return "Stack has less than 2 items."
    # xx = str(id)
    # return str(StacksHolder)

@app.route('/calc/<int:id>/divide')
def div(id):
    checkRequest(id)
    if StacksHolder[id].hasTwoItems():
        return str(StacksHolder[id].div())
    return "Stack has less than 2 items."
    # xx = str(id)
    # return str(StacksHolder)

if __name__ == "__main__":
    # app.debug = True
    app.run(host='0.0.0.0')
