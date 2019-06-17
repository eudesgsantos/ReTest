from flask import Flask, flash, redirect, render_template, request, session, abort
from pingsite import app
from pingsite.models import models
from pingsite.Forms import Lugarform

@app.route("/")
def home():
    form = Lugarform()
    return render_template('tela1.html',form=form)

@app.route("/problema")
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
