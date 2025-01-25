from flask import Flask
from flask_restful import Resource, Api

app=Flask(__name__)
print(__name__)
api=Api(app)

class Hello(Resource):
    def get(self,name):
        #return {f'Hello GoodMorning {name}'}
        return {"message": f"Hello, {name}! GoodMorning"}
    
api.add_resource(Hello,'/hello/<string:name>')

if __name__=='__main__':
    app.run(debug=True)