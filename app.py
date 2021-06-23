from flask import Flask, render_template
from flask import request
import pickle
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('index.html')


def ValuePredictor(to_predict_list):
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict_list)
    return result[0]
  
@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        print(to_predict_list)
        # to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)  
        print(result)      
        if int(result)== 0:
            prediction ='Empty'
        elif int(result)==1:
            prediction ='Sadness'  
        elif int(result)==2:
            prediction ='Enthusiasm'  
        elif int(result)==3:
            prediction ='Neutral'  
        elif int(result)==4:
            prediction ='Worry'  
        elif int(result)==5:
            prediction ='Surpise'  
        elif int(result)==6:
            prediction ='Love'  
        elif int(result)==7:
            prediction ='Fun'  
        elif int(result)==8:
            prediction ='Hate'  
        elif int(result)==9:
            prediction ='Happiness'  
        elif int(result)==10:
            prediction ='Boredom'  
        elif int(result)==11:
            prediction ='Relef'
        elif int(result)==12:
            prediction ='Anger'  

        return render_template("result.html", prediction = prediction)


if __name__ == '__main__':
   app.run()
