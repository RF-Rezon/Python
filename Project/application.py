import pickle
from flask import Flask, request, jsonify, render_template

application = Flask(__name__)
app = application

# importing models and standered scaler pickle

scaler = pickle.load(open('./models/scaler.pkl','rb'))
model_lassoCV = pickle.load(open('./models/lassoCV.pkl','rb'))

# @app.route('/')
# def welcome():
#     return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Temperature = float(request.form.get('Temperature'))
        Rh = float(request.form.get('Rh'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        DC = float(request.form.get('DC'))
        ISI = float(request.form.get('ISI'))
        BUI = float(request.form.get('BUI'))
        Classes = float(request.form.get('Classes'))

        new_data_scaled=scaler.transform([[Temperature,Rh,Ws, Rain, FFMC, DMC, DC, ISI, BUI, Classes]])
        result=model_lassoCV.predict(new_data_scaled)

        return render_template('index.html', prediction_text=result[0])

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)