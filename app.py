from flask import Flask
from resource.deadline import deadlineModule

app = Flask(__name__)
app.register_blueprint(deadlineModule, url_prefix='/api/deadline/')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
