import os
from flask import Flask, render_template
from flask import request
import requests
import ast

app = Flask(__name__)

def get_t5_response(text):
    r = requests.post(
        url="https://hf.space/embed/jaimin/FastT5/+/api/predict",
        json={"data": [text]},
    )
    response = r.json()
    return response["data"][0],response["data"][1]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form
        result = []
        result1 = []
        question = form['question']
        text1,text2 = get_t5_response(question)
        text1 = ast.literal_eval(text1)
        text2 = ast.literal_eval(text2)
        result.append(text1)
        result.append(form['question'])
        result1.append(text2)
        result1.append(form['question'])
        final_res = {
            "result": result,
            "result1": result1
        }
        return final_res

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

