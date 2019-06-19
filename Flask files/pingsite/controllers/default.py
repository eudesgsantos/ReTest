from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from pingsite import app, db, bcrypt
from pingsite.models import models
from pingsite.Forms import Lugarform
from pingsite.Forms import Loginform
from pingsite import Forms
from pingsite.models.models import Report
canudo = ['cvjso']
lista_suprema = [
'at',
'avca',
'akw',
'ayms',
'arc3',
'bsm',
'bbbgc',
'cvjso',
'cba',
'csef',
'crsm',
'drnb',
'dsa',
'dnio',
'damo',
'eemb',
'esv',
'earo',
'emfd',
'eljs',
'eess',
'fwsp',
'gsmf',
'gnp2',
'gm',
'gtb',
'hsag',
'hbf',
'hrs',
'hss',
'jcsc',
'jfcd',
'jmsda',
'jp',
'jvdc',
'jvmc',
'jvmls',
'jvca',
'jsaa',
'jcrm',
'kbcv',
'kms',
'lvco',
'lms',
'lcf',
'lfv',
'lfps',
'lml',
'lns',
'lns2',
'lra2',
'lat',
'ltf',
'ladccc',
'lfmm',
'lmbc',
'mcs',
'mlaj',
'mjsv',
'miam',
'mlml',
'mabr',
'mda',
'mcfv',
'mcla',
'msn',
'mvn',
'nbvs',
'ofn',
'phmt',
'phbbp',
'phsv',
'pqla',
'pbv',
'rdr',
'tmo',
'vrss',
'vrgf',
'wfl',
'fsf'
]

@app.route("/", methods=['GET','POST'])
def home():
    form = Lugarform()
    if request.method =="POST" and form.validate():
        place = form.lugarF.data
        problem = form.problemas.data
        extr = form.extra.data
        realprob = problem+extr
        confi02 = 1
        report = Report(lugar=form.lugarF.data, problema=form.problemas.data, extra=form.extra.data)
        db.session.add(report)
        db.session.commit() 
        return redirect(url_for('login'))
    return render_template('tela1.html',form=form)

@app.route("/VerifiqueSeuEmail")
def final():
    return render_template('tela3.html')

@app.route("/login", methods=['GET','POST'])
def login():
    form = Loginform()
    if request.method =="POST" and form.validate():
        nom = form.nomeF.data
        escol = form.hole.data
        ema = nom + escol
        confi01 = 1
        if nom in lista_suprema:
            return redirect(url_for('final'))
        
    return render_template('login.html',form=form)