from extensions import db
from sqlalchemy import text 

def obtenerReservas(user_id):
    
    sql=text('SELECT * from reservas where id_usuario = :user_id')
    
    return db.session.execute(sql,{
        'user_id':user_id
    }).fetchall()
    
    
def obtenerAllReservas():
    
    sql=text('SELECT * from reservas')
    
    return db.session.execute(sql,{}).fetchall()