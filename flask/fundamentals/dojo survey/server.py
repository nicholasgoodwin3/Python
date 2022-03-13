from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)

app.secret_key="green bean beanie boyz"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process',methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    session['windows'] = request.form['windows']
    session['mac'] = request.form['mac']
    session['linux'] = request.form['mac']
    session['PC'] = request.form['PC']
    session['macs'] = request.form['macs']
    session['unlisted'] = request.form['unlisted']

@app.route('/result')
def success():
    return render_template('index2.html')
    
if __name__=="__main__":
    app.run(debug=True)
