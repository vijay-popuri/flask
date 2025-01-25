from flask import Flask
from flask_restful import Resource,abort,reqparse,Api

app=Flask(__name__)
api=Api(app)

todoDict={
    1:{"task":"Need to learn Python", "summary":"Learn starting from scratch"},
    2:{"task":"Need to LEarn SpringBoot", "summary":"Need to Learn SpringBoot as well"}
}
parser=reqparse.RequestParser()
parser.add_argument('task', type=str, required=True, help='it is require please give what is task')
parser.add_argument('summary', type=str, required=True, help='summary is mandatory')

class ToDoList(Resource):
    def get(self):
        return todoDict
    
    def post(self,todoId):
        if todoId in todoDict:
            abort(400,message='it is already existed')
        args= parser.parse_args()
        todoDict[todoId]={"task":args["task"], "summary":args["summary"]}
        return {"message":"data saved successfully"}
    def put(self,todoId):
        if todoId not in todoDict:
            return abort(400,message='record is not present')
        args=parser.parse_args()
        todoDict[todoId]={"task":args["task"],"summary":args["summary"]}
        return {"message":"DataUpdated Successfully"}
    
    def delete(self,todoId):
        if todoId not in todoDict:
            abort(400, message="record is not present")
        del todoDict[todoId]
        return {"message":"data is deleted successfully"}
class Todo(Resource):
    def get(self,todoId):
        return todoDict[todoId]



api.add_resource(ToDoList, '/getTodos', endpoint='getTodos')
api.add_resource(Todo, '/getTodoById/<int:todoId>',endpoint='getTodoById')
api.add_resource(ToDoList, '/createTodo/<int:todoId>', endpoint='createTodo')
api.add_resource(ToDoList, '/updateTodo/<int:todoId>', endpoint='updateTodo')
api.add_resource(ToDoList, '/delete/<int:todoId>', endpoint='deleteTodo')




if __name__=='__main__':
    app.run(debug=True)