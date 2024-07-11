from flask import Flask, redirect, url_for, render_template, request, jsonify, send_file
from os import getcwd
from os.path import exists, join
from numpy import savetxt, loadtxt, asarray
from pandas import DataFrame
from pathlib import Path
import pickle
import sys

app = Flask(__name__)
current_directory = getcwd()

# This function basically writes the html page
@app.route("/")  # url for routing
def homePage():
    return render_template('web/index.html')

# API of prediction
@app.route("/api/<json_var>")
def apiRequest(json_var: str):
    pass

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        columns = ['ac_000', 'ag_006', 'ah_000', 'ay_006', 'ay_008', 'az_004',
                   'cd_000', 'cs_006', 'cv_000', 'du_000', 'eb_000']
        naive_bayes_model = pickle.load(open("static/model/naive_bayes_variance.pkl", "rb"))
        features = DataFrame([[int(request.form.get(column)) for column in columns]], columns=columns)
        prediction = naive_bayes_model.predict(features)[0]
        return redirect(url_for("response", prediction=prediction))
    return render_template("web/predict.html", prediction="no_prediction")

@app.route("/reponse")
def response():
    prediction = request.args.get('prediction', default='No prediction provided')
    return render_template('web/response.html', prediction=prediction)

@app.route("/contact")
def contact():
    return render_template("web/contact.html")

@app.route("/update")
@app.route("/update/<var>")
def update(var=""):
    if var:
        return render_template("web/update.html",var=var)
    return render_template("web/update.html")

@app.route("/submit_file_upload",methods=["POST"])
def submitFileUpload():
    if request.method=="POST":
        #At this place must be a a password encryption for client side, then hashing with a salt number retired from a database, after that a comparition of the hashed passwords and then the password will be verified
        ID = request.form.get("identification")
        pw = request.form.get("password")
        if ID=="0000" and pw == "123456789":
            return redirect(url_for("homePage"))
        else:
            return redirect(url_for("update",var="bad"))


@app.route('/<some_url>')
def method_name(some_url):
    return render_template("web/notFound.html")

if __name__ == "__main__":
    '''
    # To serve in a production environment use pywsgi.WSGIServer after creating the server.key and server.crt with OpenSSL for example
    # -------------------------------------------Code--------------------------------------------------
    http_server = pywsgi.WSGIServer(('0.0.0.0', 443), application=app, keyfile='server.key', certfile='server.crt')
    http_server.serve_forever()
    # --------------------------------------------------------------------------------------------------
    '''
    app.run(host='0.0.0.0', debug=True)
