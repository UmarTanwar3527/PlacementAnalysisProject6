import numpy as np
from flask import Flask, request, jsonify, render_template
# from flask_ngrok import run_with_ngrok
import pickle


app = Flask(__name__)
model_RF=pickle.load(open('PlacementAnalysis_NB.pkl', 'rb')) 
model_DT=pickle.load(open('PlacementAnalysis_KNN.pkl', 'rb')) 
model_KNN=pickle.load(open('PlacementAnalysis_DT.pkl', 'rb')) 
model_LC=pickle.load(open('PlacementAnalysis_SVM_linear.pkl', 'rb')) 
model_K_SVM=pickle.load(open('PlacementAnalysis_SVM_RBF.pkl', 'rb')) 
model_SVM=pickle.load(open('PlacementAnalysis_SVM_Sigmoid.pkl', 'rb')) 
model_NB=pickle.load(open('PlacementAnalysis_RF.pkl', 'rb')) 
# run_with_ngrok(app)

@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    ten = float(request.args.get('ten'))
    twell = float(request.args.get('twell'))
    btech = float(request.args.get('btech'))
    seven = float(request.args.get('seven'))
    six = float(request.args.get('six'))
    five = float(request.args.get('five'))
    final = float(request.args.get('final'))
    med = float(request.args.get('med'))
    
    prediction = model_RF.predict([[ten, twell, btech, seven, six, five, final, med]])
    
    if prediction == [1]:   
      return render_template('index.html', prediction_text='Congratulations you will be Placed.')
    else:
      return render_template('index.html', prediction_text='Sorry you will not be Placed, Better Luck next Time.')

if __name__ == '__main__':
  app.run(debug=True)
