from flask import Flask, render_template

app=Flask(__name__)

    
from main.routes import main
from login.routes import login

app.register_blueprint(main)
app.register_blueprint(login)



if __name__=='__main__':
    app.run(debug=True)