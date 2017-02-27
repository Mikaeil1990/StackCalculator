""" RESTful-API using Flask Framework.
================================================================
Below is the list of endpoints:
End-points:

/calc/:id/peek :        returns stack[top]
/calc/:id/push/<n> :    pushes a number onto the stack
/calc/:id/pop :         returns the top from the stack and removes it
/calc/:id/add :         removes the top and top-1 from the stack and replaces it with stack[top-1]+stack[top]
/calc/:id/subtract :    removes the top and top-1 from the stack and replaces it with stack[top-1]-stack[top]
/calc/:id/multiply :    removes the top and top-1 from the stack and replaces it with stack[top-1]*stack[top]
/calc/:id/divide :      removes the top and top-1 from the stack and replaces it with stack[top-1]/stack[top]

"""
from flask import Flask, render_template
from Model.Stack import Stack

# Creating a Flask object and configure it
app = Flask(__name__)
app.config.from_pyfile('app.cfg')

# A dictionary pairing Stacks to their id. This is the resource of server.
StacksHolder = {}

def checkRequest(id):
    """ For each request this func checks the Stack number exist or not. in case of not found it creates one."""
    flag_stackExist = False
    for key, value in StacksHolder.iteritems():
        if key == id:
            flag_stackExist = True
    if flag_stackExist == False:
        StacksHolder[id] = Stack()


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/calc/<int:id>/peek')
def peek(id):
    """Index endpoint which renders a template with some example of calls."""
    checkRequest(id)
    if StacksHolder[id].isEmpty():
        return "Stack is Empty."
    return str(StacksHolder[id].peek())

@app.route("/calc/<int:id>/push/<int:n>")
def push(id, n):
    """Push endpoint which Add a number to selected stack."""
    checkRequest(id)
    res = StacksHolder[id].push(n)
    return res

@app.route('/calc/<int:id>/pop')
def pop(id):
    """pop endpoint which return Top number of selected stack."""
    checkRequest(id)
    if StacksHolder[id].isEmpty():
        return "Stack is Empty."
    return str(StacksHolder[id].pop())

@app.route('/calc/<int:id>/add')
def add(id):
    """add endpoint which return the result of adding the top 2 numbers of selected stack."""
    checkRequest(id)
    if StacksHolder[id].hasTwoItems():
        return str(StacksHolder[id].add())
    return "Stack has less than 2 items."

@app.route('/calc/<int:id>/subtract')
def sub(id):
    """sub endpoint which return the result of subtracting the top 2 numbers of selected stack."""
    checkRequest(id)
    if StacksHolder[id].hasTwoItems():
        return str(StacksHolder[id].sub())
    return "Stack has less than 2 items."

@app.route('/calc/<int:id>/multiply')
def mul(id):
    """multiply endpoint which return the result of multiplying the top 2 numbers of selected stack."""
    checkRequest(id)
    if StacksHolder[id].hasTwoItems():
        return str(StacksHolder[id].mul())
    return "Stack has less than 2 items."


@app.route('/calc/<int:id>/divide')
def div(id):
    """divide endpoint which return the result of dividing the top 2 numbers of selected stack."""
    checkRequest(id)
    if StacksHolder[id].hasTwoItems():
        return str(StacksHolder[id].div())
    return "Stack has less than 2 items."
    # xx = str(id)
    # return str(StacksHolder)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
