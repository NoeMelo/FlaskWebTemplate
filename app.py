from flask import Flask, render_template, redirect, request, url_for

#import NLP model predict function
from nlpmodel import predict

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def index():
    if request.method == "POST":
        #get comments input from interface
        comments = request.form["comments"]
        #predict comments
        result = predict(comments)
    else:
        result = ""
    return render_template('index.html',result=result)

if __name__ == "__main__":
    app.run(debug=True)