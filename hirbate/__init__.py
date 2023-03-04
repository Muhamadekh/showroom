from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ca756c5133bfd45cb5f1ff0c7a21d624'

from hirbate import routes