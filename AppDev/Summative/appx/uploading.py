from flask import Flask,render_template,request,redirect,url_for
import pandas as pd
import csv

app = Flask(__name__)

@app.route('/upload_file', methods=['GET','POST'])
def upload_file():
    return render_template('upload_file.html',msg="Please Choose")
if __name__=='__main__':
    app.run()