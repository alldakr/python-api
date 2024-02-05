from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoResource(Resource):
    def get(self, todo_id):
        return {todo_id: todos.get(todo_id, 'Todo not found')}

    def put(self, todo_id):
        parser = reqparse.RequestParser()
        parser.add_argument('task')
        args = parser.parse_args()
        todos[todo_id] = args['task']
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        if todo_id in todos:
            del todos[todo_id]
            return {'result': 'Todo deleted'}
        else:
            return {'result': 'Todo not found'}

class TodoListResource(Resource):
    def get(self):
        return todos

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('task')
        args = parser.parse_args()
        todo_id = max(map(int, todos.keys())) + 1
        todos[todo_id] = args['task']
        return {todo_id: todos[todo_id]}

class Todo(Resource):
    def get(self):
        return todos


api.add_resource(TodoResource, '/todos/<int:todo_id>')
api.add_resource(TodoListResource, '/todos')
api.add_resource(Todo, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
