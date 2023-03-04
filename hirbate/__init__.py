from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ca756c5133bfd45cb5f1ff0c7a21d624'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

with app.app_context():
    db.create_all()




from hirbate import routes