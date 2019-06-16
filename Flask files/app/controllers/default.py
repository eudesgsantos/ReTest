from app import app
from flask import Flask, flash, redirect, render_template, request, session, abort

@app.route("/")
def home():
    return render_template('tela1.html')

@app.route("/tela2.html")
def seg():
    return render_template('tela2.html')

@app.route("/tela3.html")
def ter():
    return render_template('tela3.html')

@app.route('/login', methods = ['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password or login')
        return home()
