from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from sqlalchemy import text 
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from flask import jsonify, request

area=Blueprint("area",__name__)


@area.route('/anadir_tarea', methods=['POST'])

def anadir_tarea():
    
    if request.method=='POST':
        fecha_reserva=request.form['fecha-cita']
        hora_reserva=request.form['hora-cita']
        fecha_hora_reserva = f"{fecha_reserva} {hora_reserva}:00"
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


@area.route("/borrar_reserva", methods=['POST'])

def borrar_reserva():
    reserva_id=request.form['reserva_id']
    
    sql=text('DELETE FROM reservas WHERE id = :reserva_id')
    
    db.session.execute(sql,{
        'reserva_id':reserva_id
    })
    
    db.session.commit()
    
    return redirect(url_for('login.area'))



@area.route("/obtener_horas_disponibles")
def obtener_horas_disponibles():
    
    fecha_seleccionada = request.args.get('fecha')
    horas_totales = ["09:00", "10:00", "11:00", "12:00", "13:00", "16:00", "17:00", "18:00"]

    sql = text("""
        SELECT TO_CHAR(fecha_reserva, 'HH24:MI') as hora 
        FROM reservas 
        WHERE CAST(fecha_reserva AS DATE) = :fecha
    """)
    
    resultado = db.session.execute(sql, {'fecha': fecha_seleccionada})
    
    horas_ocupadas = [fila[0] for fila in resultado]
    
    # Limpiamos los posibles espacios en blanco si los hubiera
    horas_ocupadas = [h.strip() for h in horas_ocupadas]

    # Filtramos
    horas_libres = [h for h in horas_totales if h not in horas_ocupadas]
    
    return jsonify(horas_libres)