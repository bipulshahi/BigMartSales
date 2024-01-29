#Server File
#pip3 install Flask

from flask import Flask
import util


app = Flask(__name__)

@app.route("/")
def Big_Mart_Sales():
    return "Welcome to Big Mart Sales Value Prediction"

@app.route("/show_feature_names")
def show_feature_names():
    response = {"Data Columns" : util.show_feature_names()}
    return response


app.run()
