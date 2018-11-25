from flask import Flask
from flask_restful import Resource, Api,request, abort
from sklearn.externals import joblib

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

class HelloWorld(Resource):
    def post(self):
        classifier = joblib.load('model.pkl')
        value_1 = request.get_json(force=True)['value_1']
        value_2 = request.get_json(force=True)['value_2']
        result = float(classifier.predict([[value_1,value_2]])) * 1000
		
        return {'result': result }


class Hello(Resource):
    def get(self):
        print('API GET ')
        return 'API GET'

class Dise(Resource):
    def get(self):
        print("csasw")  
        return 'cs'         


api.add_resource(HelloWorld, '/')
api.add_resource(Hello, '/hello')
api.add_resource(Dise,'/dise')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5080 )