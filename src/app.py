from flask import Flask
from flask import jsonify
from flask import request
import json
app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todos.pop(id)
    return jsonify(todos)


#These two line should always be at the end of your app.py file
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)