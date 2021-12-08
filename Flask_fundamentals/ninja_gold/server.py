from flask import Flask, request, redirect, render_template, session
import random
app = Flask(__name__)
app.secret_key = "srecet yek"

@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def proccess_money():
    if request.form['building'] == "farm":
        amount = random.randint(10,20)
        session['count'] += amount
    elif request.form['building'] == "cave":
        amount = random.randint(5,10)
        session['count'] += amount
    elif request.form['building'] == "house":
        amount = random.randint(2,5)
        session['count'] += amount
    elif request.form['building'] == "casino":
        amount = random.randint(-50,50)
        session['count'] += amount
    if 'message' not in session:
        if amount > 0:
            session['message'] = f"<p>You earned {amount} gold from {request.form['building']} </p>"
    elif amount > 0:
        session['message'] += f"<p>You earned {amount} gold from {request.form['building']} </p>"
    else: 
        session['message'] += f"<p>You lost {amount} gold from {request.form['building']} </p>"
    return redirect('/')

@app.route('/reset')
def reset_gold():
    session.clear()
    return redirect('/')
if __name__=="__main__":   
    app.run(debug=True)   
