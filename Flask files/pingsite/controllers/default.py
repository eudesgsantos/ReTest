from flask import Flask, flash, redirect, render_template, request, session, abort
from pingsite import app, db, bcrypt
from pingsite.models import models
from pingsite.Forms import Lugarform
from pingsite.Forms import Loginform, ProblemasForm
@app.route("/")
def home():
    form = Lugarform()
    return render_template('tela1.html',form=form)

@app.route("/problema")
def seg():
    form = ProblemasForm()
    return render_template('tela2.html',form=form)

@app.route("/tela3.html")
def ter():
    return render_template('tela3.html')

@app.route("/login")
def login():
    form = Loginform()
    return render_template('login.html',form=form)