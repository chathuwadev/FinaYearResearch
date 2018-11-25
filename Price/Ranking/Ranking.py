
from algoliasearch import algoliasearch
from flask import Flask
from flask_restful import Resource, Api,request, abort
from sklearn.externals import joblib

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import dateutil.parser

application = Flask(__name__)
Rapi = Api(application)

class HelloWorld(Resource):

client = algoliasearch.Client("OYSCK559RX", 'f62fcecc0810869b90088c2ed6a21b27')
index = client.init_index('iFarmer')

index = client.init_index("shop")
batch = json.load(open('shops.json'))
index.add_objects(batch)

index.setSettings({
  customRanking: [
    'asc(rating)',
    'asc(location)',
	'true(availability)'
  ]
});