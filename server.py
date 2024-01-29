#Server File
#pip3 install Flask

from flask import Flask,request
import util


app = Flask(__name__)

@app.route("/")
def Big_Mart_Sales():
    return "Welcome to Big Mart Sales Value Prediction"

@app.route("/show_feature_names")
def show_feature_names():
    response = {"Data Columns" : util.show_feature_names()}
    return response

@app.route('/predict_sales',methods=['POST'])
def show_predicted_sales():
    item_ide1 = request.form['id1']
    item_ide2 = float(request.form['id2'])
    item_fat_content = request.form['ifc']
    item_type = request.form['it']
    out_size = request.form['os']
    out_loc_type = request.form['olt']
    out_type = request.form['ot']
    item_weight = float(request.form['iw'])
    item_visibility = float(request.form['iv'])
    item_mrp = float(request.form['im'])
    out_ide = float(request.form['oid'])
    out_age = float(request.form['oa'])

    sales = util.predict_sales(item_ide2,item_weight,item_visibility,item_mrp,
                               out_ide,out_age,item_ide1,item_fat_content,
                               item_type,out_size,out_loc_type,out_type)

    response = {"predicted Sales" : sales}
    return response

app.run()
