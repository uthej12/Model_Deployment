from flask import Flask, render_template,request
import pickle
import numpy as np


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        model = pickle.load(open('model.sav', 'rb'))

        cp = int(request.form['cp'])
        max_heart = int(request.form['max_heart'])
        angia = int(request.form['agnia'])
        st = float(request.form['st'])

        res = model.predict([[cp,max_heart,angia, st]])

        if res[0] == 1:
            text = 'High Chances of getting a heart disease'
        elif res[0] == 0:
            text = 'Low Chances of getting a heart disease'

        return render_template('predict.html',show = True, res = text)
    else:
        return render_template('predict.html',show = False)


if __name__ == '__main__':
    app.run()
