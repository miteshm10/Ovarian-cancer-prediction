from flask import Flask, request,render_template
import pickle
import numpy as np


model = pickle.load(open('C:\Machine Learnig\Flask\env\ovary_cancer.pickle', 'rb'))


app=Flask(__name__)

@app.route('/')
def man():
    return render_template("index.html")


@app.route("/predict",methods=["POST"])
def home():
    data1 = request.form['1_FormBinaryValue_Age']
    data2 = request.form['2_FormBinaryValue_CEA (ng/ml)']
    data3 = request.form['3_FormBinaryValue_CA125 (U/ml)']
    data4 = request.form['4_FormBinaryValue_CA19-9 (U/ml)']
    data5 = request.form['5_FormBinaryValue_HE4 (pmol/L)']
    data6 = request.form['6_FormBinaryValue_CREA (umol/l)']
    data7 = request.form['7_FormBinaryValue_ALT (u/l)']
  
    arr = np.array([[data1, data2, data3, data4,data5,data6,data7]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)



if __name__=="__main__":
    app.run(debug=True)
