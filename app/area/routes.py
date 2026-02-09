from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from sqlalchemy import text 
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

area=Blueprint("area",__name__)


@area.route('/anadir_tarea', methods=['POST'])

def anadir_tarea():
    
    if request.method=='POST':
        fecha_reserva=request.form['fecha-cita']
        hora_reserva=request.form['hora-cita']
        fecha_hora_reserva=fecha_reserva + " "+ hora_reserva
        id_usuario=session['user_id']
        motivo_cita=request.form['motivo-cita']
        matricula=request.form['matricula']
        
        sql=text('INSERT INTO reservas (fecha_reserva,id_usuario,motivo_cita,matricula) VALUES (:fecha_reserva, :id_usuario, :motivo_cita, :matricula)')
        
        db.session.execute(sql,{
            'fecha_reserva':fecha_hora_reserva,
            'id_usuario':id_usuario,
            'motivo_cita':motivo_cita,
            'matricula':matricula
        })
        
        db.session.commit()
        
        return redirect(url_for('login.area'))
        
    return redirect(url_for('login.area'))