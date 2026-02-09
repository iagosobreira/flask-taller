from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from sqlalchemy import text 
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from functools import wraps

login=Blueprint('login',__name__)

@login.route('/crear_usuario', methods=['POST'])

def crear_usuario():
    if request.method=='POST':
        
        nombre= request.form['nombre']
        correo=request.form['correo']
        contrasena=request.form['contrasena']
        contrasena_hash = generate_password_hash(contrasena)
        
        sql=text('INSERT INTO usuarios (nombre, correo, contrasena, rol) VALUES (:nombre, :correo, :contrasena_hash, :rol)')
        
        db.session.execute(sql,{
            'nombre':nombre,
            'correo':correo,
            'contrasena_hash':contrasena_hash,
            'rol':'usuario'
        })
        
        db.session.commit()
        
        return redirect(url_for('main.inicio'))
    
    
    else:
        return redirect(url_for("main.inicio_registro"))
    

@login.route("/iniciar_sesion", methods=['POST'])

def iniciar_sesion():
    
    if request.method=='POST':
        correo=request.form['correo']
        contrasena=request.form['contrasena']
        
        sql=text('SELECT * FROM usuarios WHERE correo = :correo')
        
        result= db.session.execute(sql,{
            'correo':correo
        }).fetchone()
        
        if result and check_password_hash(result.contrasena, contrasena):
            session['user_id']=result.id
            session['user_name']=result.nombre
            
            return redirect(url_for('login.area'))
        
    return 
        

    
    
    
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


@login.route("/area")
@login_required
def area():
    if 'user_id' not in session:
        return redirect(url_for('main.inicio_login'))
        
        
    return render_template('area.html',usuario=session['user_name'])
    



@login.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.inicio_login"))