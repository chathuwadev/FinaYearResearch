from flask import Flask
from flask_restful import Resource, Api,request, abort
from sklearn.externals import joblib

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import dateutil.parser

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def post(self):
        
        #value_1 = dateutil.parser.parse(request.get_json(force=True)['value_1'])
        value_1 = request.get_json(force=True)['value_1']
       
		
        

        df=pd.read_csv('price_production_daily.csv')
        df['datetime'] = pd.to_datetime(df['date'])
        df.set_index('datetime', inplace=True)
        df = df.sort_index(ascending=True)
        #df.tail(20)
        #model1=sm.OLS(endog=df['price'],exog=df['production'])
        #results1=model1.fit()
        df['diffprice']=df['price'].diff()
        df['diffproduction']=df['production'].diff()
        model2=sm.OLS(endog=df['diffprice'].dropna(),exog=df['diffproduction'].dropna())
        results2=model2.fit()
        df['lag']=df['diffproduction'].shift()
        df.dropna(inplace=True)
        df_val = df.loc[df.index >= str(value_1)]
        df_train = df.loc[df.index < str(value_1)]
        model3=sm.tsa.ARIMA(endog=df_train['price'],exog=df_train['lag'],order=[1,0,2])
        results3=model3.fit()
        re=results3.forecast(steps=len(df_val['lag']), exog=df_val['lag'])[0][0]

        print(value_1)

        return {'result': re }

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
    app.run(debug=True,host='0.0.0.0',port=5081)