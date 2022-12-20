from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS 
from all_query import user_query, todo_query
# import socket

app = Flask(__name__)
api = Api(app)

# 設定CORS特定網域使用api
CORS(
    app
)

class helloworld(Resource):

    def get(self):
        return {'hello': 'world'}

user_login_parser = reqparse.RequestParser()
user_login_parser.add_argument('account', type=str, help='account of login is required.', required=True)
user_login_parser.add_argument('password', type=str, help='password of login is required.', required=True)

user_register_parser = reqparse.RequestParser()
user_register_parser.add_argument('account', type=str, help='account of register is required.', required=True)
user_register_parser.add_argument('password', type=str, help='password of register is required.', required=True)

class User(Resource):

    def get(self):
        return {'user': 'api addr'}

    # login
    def post(self):
        args = user_login_parser.parse_args()
        account = args['account']
        password = args['password']
        session_id = user_query.login(account, password)
        if session_id != False:
            return {'s_id': session_id}, 200
        else:
            return {'s_id': 'NotUser'}, 404

    def put(self):
        args = user_register_parser.parse_args()
        status = user_query.create_user(args['account'], args['password'])
        if status == True:
            return {'status': '不錯👍'}, 200
        else:
            return {'status': 'ㄟ ㄌㄨㄛˇ'}, 404

add_todo_parser = reqparse.RequestParser()
add_todo_parser.add_argument('s_id', type=str, help='s_id of todo is required.', required=True)
add_todo_parser.add_argument('title', type=str, help='Title of todo is required.', required=True)
add_todo_parser.add_argument('content', type=str, help='Content of todo is required.', required=True)

select_todo_parser = reqparse.RequestParser()
select_todo_parser.add_argument('s_id', type=str, help='s_id of select todo is required.', required=True)

delete_todo_parser = reqparse.RequestParser()
delete_todo_parser.add_argument('s_id', type=str, help='todo_id of delete todo is required.', required=True)
delete_todo_parser.add_argument('todo_id', type=int, help='todo_id of delete todo is required.', required=True)

class Todo(Resource):

    def post(self):
        args = select_todo_parser.parse_args()
        s_id = args['s_id']
        return todo_query.select(s_id), 200

    def put(self):
        args = add_todo_parser.parse_args()
        s_id = args['s_id']
        title = args['title']
        content = args['content']
        status = todo_query.add(s_id, title, content)
        if status == True:
            return {'status': '不錯👍'}, 200
        else:
            return {'status': 'ㄟ ㄌㄨㄛˇ'}, 404

    def delete(self):
        args = delete_todo_parser.parse_args()
        s_id = args['s_id']
        todo_id = args['todo_id']
        status = todo_query.delete(s_id, todo_id)
        if status == True:
            return {'status': '不錯👍'}, 200
        else:
            return {'status': 'ㄟ ㄌㄨㄛˇ'}, 404

api.add_resource(helloworld, '/')
api.add_resource(User, '/User')
api.add_resource(Todo, '/Todo')

if __name__ == '__main__':
    app.run(debug=True)
