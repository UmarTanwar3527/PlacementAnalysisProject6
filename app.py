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


# def predict_random(UserID, Gender,Age,EstimatedSalary):
#   output= model_randomforest.predict(sc.transform([[Age,EstimatedSalary]]))
#   print("Purchased", output)
#   if output==[1]:
#     prediction="Item will be purchased"
#   else:
#     prediction="Item will not be purchased"
#   print(prediction)
#   return prediction
# def main():
    
#     html_temp = """
#    <div class="" style="background-color:blue;" >
#    <div class="clearfix">           
#    <div class="col-md-12">
#    <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
#    <center><p style="font-size:30px;color:white;margin-top:10px;">Department of Computer Engineering</p></center> 
#    <center><p style="font-size:25px;color:white;margin-top:10px;"Machine Learning Lab Experiment</p></center> 
#    </div>
#    </div>
#    </div>
#    """
#     st.markdown(html_temp,unsafe_allow_html=True)
#     st.header("Item Purchase Prediction using SVM Algorithm")
#     UserID = st.text_input("UserID","")
#     Gender = st.selectbox(
#     "Gender",
#     ("Male", "Female", "Others")
#     )
    
#     Age = st.number_input('Insert a Age',18,60)
#     #Age = st.text_input("Age","Type Here")
#     EstimatedSalary = st.number_input("Insert EstimatedSalary",15000,150000)
#     resul=""
#     if st.button("SVM Prediction"):
#       result=predict_note_authentication(UserID, Gender,Age,EstimatedSalary)
#       st.success('SVM Model has predicted {}'.format(result))
#     if st.button("Random Forest Prediction"):
#       result=predict_random(UserID, Gender,Age,EstimatedSalary)
#       st.success('Random forest Model  has predicted {}'.format(result))  
#     if st.button("About"):
#       st.header("Developed by Mohammed Umar Tanwar")
#       st.subheader("Head , Department of Computer Engineering")
#     html_temp = """
#     <div class="" style="background-color:orange;" >
#     <div class="clearfix">           
#     <div class="col-md-12">
#     <center><p style="font-size:20px;color:white;margin-top:10px;">Machine Learning Experiment 5: Support Vector Machine and Random Forest</p></center> 
#     </div>
#     </div>
#     </div>
#     """
#     st.markdown(html_temp,unsafe_allow_html=True)
# if __name__=='__main__':
#   main()