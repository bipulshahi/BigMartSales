#create an utility file
#access artifacts and create a prediction function

import numpy as np
import pickle
import json
import pandas as pd

features = ''
_model = ''
_scaling = ''

def read_artifacts():

    global features
    global _model
    global _scaling
    
    #access the json file with feature name information
    with open('salesprojectfeatures.json','r') as f:
      features = json.load(f)['features']

    #access the model pickle file
    with open('salesmodel.pkl','rb') as f:
      _model = pickle.load(f)

    #access the scaling pickle file
    with open('featurescaling.pkl','rb') as f:
      _scaling = pickle.load(f)


def predict_sales(item_ide2,item_weight,item_visibility,item_mrp,out_ide,out_age,
                  item_ide1,item_fat_content,item_type,out_size,out_loc_type,out_type):
    input_data = np.zeros(len(features))

    input_data[0] = item_ide2
    input_data[1] = item_weight
    input_data[2] = item_visibility
    input_data[3] = item_mrp
    input_data[4] = out_ide
    input_data[5] = out_age

    input_data[features.index('Item_Identifier1_' + item_ide1)] = 1
    input_data[features.index('Item_Fat_Content_' + item_fat_content)] = 1
    input_data[features.index('Item_Type_' + item_type)] = 1
    input_data[features.index('Outlet_Size_' + out_size)] = 1
    input_data[features.index('Outlet_Location_Type_' + out_loc_type)] = 1
    input_data[features.index('Outlet_Type_' + out_type)] = 1

    return round(np.exp(_model.predict(_scaling.transform([input_data])))[0],2)


read_artifacts()
#print(features)
print(predict_sales(14,12.5,0.08,54.5,19,10,
                    "FD","Regular","Canned","Small","Tier 2","Supermarket Type3"))
