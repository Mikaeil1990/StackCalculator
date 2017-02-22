from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('app.cfg')

@app.route("/")
def index():
    return "hello!!!"
if __name__ == "__main__":
    # app.debug = True
    app.run(host='0.0.0.0')
