from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from sqlalchemy import text 
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

admin=Blueprint('admin',__name__)

@admin.route('/cambiar_estado', methods=['POST'])

def cambiar_estado():
    
    estado_boton=request.form['estado_boton']
    
    if estado_boton=='Aceptar':
        estado='Aceptada'
    else:
        estado="Denegada"
        
    reserva_id=request.form['reserva_id']
    
    sql=text('UPDATE reservas SET estado = :estado WHERE id = :reserva_id')
    
    db.session.execute(sql, {
        "estado":estado,
        "reserva_id":reserva_id
    })
    
    db.session.commit()
    
    return redirect(url_for("login.admin_area"))