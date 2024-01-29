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

@app.route('/predict_sales')
def show_predicted_sales():
    item_ide1 = "FD"
    item_ide2 = 14
    item_fat_content = "Regular"
    item_type = "Canned"
    out_size = "Small"
    out_loc_type = "Tier 2"
    out_type = "Supermarket Type3"
    item_weight = 12.5
    item_visibility = 0.08
    item_mrp = 54.5
    out_ide = 19
    out_age = 10

    sales = util.predict_sales(item_ide2,item_weight,item_visibility,item_mrp,
                               out_ide,out_age,item_ide1,item_fat_content,
                               item_type,out_size,out_loc_type,out_type)

    response = {"predicted Sales" : sales}
    return response

app.run()
