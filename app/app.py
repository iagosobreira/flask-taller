from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template
from config import Config
from extensions import db

app=Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
    
from main.routes import main
from login.routes import login

app.register_blueprint(main)
app.register_blueprint(login)



if __name__=='__main__':
    app.run(debug=True)