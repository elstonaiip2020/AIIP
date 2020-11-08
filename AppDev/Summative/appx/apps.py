from flask import Flask,render_template,request,redirect,url_for,jsonify
import pandas as pd
import csv

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

# Upload maintenace data
@app.route('/schedule', methods=['GET','POST'])
def schedule():

    global wind_schedule
    global solar_schedule
    
    if request.method =='POST':
        f1 =request.form['solar']
        f2 =request.form['wind']
        data1={}
        data2={}
        with open(f1) as file1:
            csvfile1 = csv.reader(file1)
            for row in csvfile1:
                if type(row[1])==str and len(row[1])>0:
                    if len(row[1])>4:
                        data1[row[0]]=row[1]
                    else:
                        data1[row[0]]=float(row[1])
               
        with open(f2) as file2:
            csvfile2 = csv.reader(file2)
            for row in csvfile2:
                if type(row[1])==str and len(row[1])>0:
                    if len(row[1])>4:
                        data2[row[0]]=row[1]
                    else:
                        data2[row[0]]=float(row[1])
    solar_schedule=data1
    wind_schedule=data2
    return render_template('data.html',solar_schedule=solar_schedule,wind_schedule=wind_schedule,msg="Upload Sucessful!"),wind_schedule
 
@app.route('/test')
def test():
    print(wind_schedule)
    return
    
if __name__=='__main__':
    app.run()