from flask import Flask,render_template,app, request 
import pandas as pd
import pickle as pkl
import numpy as np
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

app=Flask(__name__,template_folder="templates")


@app.route("/",methods=["GET"])
def home():
    render_template("index.html")
    
@app.route("/predict",methods=["POST"])
def predict():
    if request.method=="POST":
        try:
            product_id=request.form["product_id"]
            Gender=request.form["gender"]
            if (Gender=="male"):
                gender=1
            else:
               gender=0
            age=int(request.form["age"])
            age_val=0
            if age>=0 and age<18:
               age_val=1
            elif age>=18 and age<26:
               age_val=2
            elif age>=26 and age<36:
               age_val=3
            elif age >= 36 and age <= 45:
                age_value = 4
            elif age >= 46 and age <= 50:
                age_value = 5
            elif age >= 51 and age <= 55:
                age_value = 6
            elif age >= 56:
                age_value = 7
            occupation=int(request.form["Occupation"])
            city=(request.form["city"])
            stay_in_city_val=request.form["staying in current city"]
            pro_cat1_val=request.form["product cat 1"]
            pro_cat2_val=request.form["product cat 2"]
            pro_cat3_val=request.form["product cat 3"]
            features=[age_val,occupation,stay_in_city_val,pro_cat1_val,pro_cat2_val,pro_cat3_val]
    
            int_features=[int(x) for x in features]
            final_features= [np.array(int_features)]

            filename="abc.sav"
            scaler_file="scaler.sav"
            
            with open(scaler_file,"rb") as scaler:
                scaler=pkl.load(scaler)
            
            with open(filename,"rb") as model:
                model=pkl.load(model)
            
            prediction=model.predict(scaler)
            
            return render_template("results.html",prediction_text='Purchase amount: {}$'.format(round(prediction[0])))

        except Exception as e:
            print("Error Occured",e)
            return "Error Occurred plzz check your backend code"

if __name__=="__main__":
    app.run(debug=True)                           
                           