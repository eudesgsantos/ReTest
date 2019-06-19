from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from pingsite import app, db, bcrypt
from pingsite.models import models
from pingsite.Forms import Lugarform
from pingsite.Forms import Loginform, ProblemasForm
from pingsite import Forms
canudo = ['cvjso']

@app.route("/")
def home():
    form = Lugarform()
    return render_template('tela1.html',form=form)

@app.route("/problema")
def seg():
    form = ProblemasForm()
    return render_template('tela2.html',form=form)

@app.route("/VerifiqueSeuEmail")
def ter():
    return render_template('tela3.html')

@app.route("/login", methods=['GET','POST'])
def login():
    form = Loginform()
    if request.method =="POST" and form.validate():
        return redirect(url_for('seg'))
        
    return render_template('login.html',form=form)