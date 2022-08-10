import numpy as np
from flask import Flask, request, jsonify, render_template
# from flask_ngrok import run_with_ngrok
import pickle


app = Flask(__name__)
'''model_RF=pickle.load(open('/content/drive/My Drive/('/content/drive/My Drive/.pkl', 'rb')) 
model_KNN=pickle.load(open('/content/drive/My Drive/PlacementAnalysis_KNN.pkl', 'rb')) 
model_DT=pickle.load(open('/content/drive/My Drive/PlacementAnalysis_DT.pkl', 'rb')) 
model_SVM_L=pickle.load(open('/content/drive/My Drive/PlacementAnalysis_SVM_linear.pkl', 'rb')) 
model_SVM_R=pickle.load(open('/content/drive/My Drive/PlacementAnalysis_SVM_RBF.pkl', 'rb')) 
model_SVM_S=pickle.load(open('/content/drive/My Drive/PlacementAnalysis_SVM_Sigmoid.pkl', 'rb')) 
model_NB=pickle.load(open('/content/drive/My Drive/PlacementAnalysis_NB.pkl', 'rb')) '''
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
    model1=float(request.args.get('model1'))
    if model1==0:
        model=pickle.load(open('PlacementAnalysis_RF.pkl','rb'))
        accr="76.67%"
    elif model1==1:
        model=pickle.load(open('PlacementAnalysis_KNN.pkl','rb'))
        accr="63.33%"
    elif model1==2:
        model=pickle.load(open('PlacementAnalysis_DT.pkl','rb'))
        accr="70.00%"
    elif model1==3:
        model=pickle.load(open('PlacementAnalysis_SVM_linear.pkl','rb'))
        accr="76.67%"
    elif model1==4:
        model=pickle.load(open('PlacementAnalysis_SVM_RBF.pkl','rb'))
        accr="63.33%"
    elif model1==5:
        model=pickle.load(open('PlacementAnalysis_SVM_Sigmoid.pkl','rb'))
        accr="63.33%"
    elif model1==6:
        model=pickle.load(open('PlacementAnalysis_NB.pkl','rb'))
        accr="73.33%"

    prediction = model.predict([[ten, twell, btech, seven, six, five, final, med]])
    if prediction==1:
         message="Congratulations! you will be Placed"
    else:
        message="Unfortunately! you will not be Placed, better luck next time"

    return render_template('index.html', prediction_text=message, accuracy_text='Accuracy of Model :{}'.format(accr))
if __name__ == "__main__":
    app.run(debug=True)

# app.run()
'''    if model == 0:
      prediction = model_RF.predict([[ten, twell, btech, seven, six, five, final, med]])
      
      if prediction == [1]:   
        return render_template('index.html', prediction_text='Booyah! you will be placed')
      else:
        return render_template('index.html', prediction_text='Unfortunately, you will not be placed, better luck next time')
      
    if model == 1:
      prediction = model_KNN.predict([[ten, twell, btech, seven, six, five, final, med]])
      
      if prediction == [1]:   
        return render_template('index.html', prediction_text='Booyah! you will be placed')
      else:
        return render_template('index.html', prediction_text='Unfortunately, you will not be placed, better luck next time')

    if model == 2:
      prediction = model_DT.predict([[ten, twell, btech, seven, six, five, final, med]])
      
      if prediction == [1]:   
        return render_template('index.html', prediction_text='Booyah! you will be placed')
      else:
        return render_template('index.html', prediction_text='Unfortunately, you will not be placed, better luck next time')

    if model == 3:
      prediction = model_SVM_L.predict([[ten, twell, btech, seven, six, five, final, med]])
      
      if prediction == [1]:   
        return render_template('index.html', prediction_text='Booyah! you will be placed')
      else:
        return render_template('index.html', prediction_text='Unfortunately, you will not be placed, better luck next time')

    if model == 4:
      prediction = model_SVM_R.predict([[ten, twell, btech, seven, six, five, final, med]])
      
      if prediction == [1]:   
        return render_template('index.html', prediction_text='Booyah! you will be placed')
      else:
        return render_template('index.html', prediction_text='Unfortunately, you will not be placed, better luck next time')

      if model == 5:
        prediction = model_SVM_S.predict([[ten, twell, btech, seven, six, five, final, med]])
        
        if prediction == [1]:   
          return render_template('index.html', prediction_text='Booyah! you will be placed')
        else:
          return render_template('index.html', prediction_text='Unfortunately, you will not be placed, better luck next time')

    if model == 6:
      prediction = model_NB.predict([[ten, twell, btech, seven, six, five, final, med]])
        
      if prediction == [1]:   
        return render_template('index.html', prediction_text='Booyah! you will be placed')
      else:
        return render_template('index.html', prediction_text='Unfortunately, you will not be placed, better luck next time')'''
 
