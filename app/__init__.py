from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "12345"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:123456@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://flezfwidwaxhvq:a51adba3c7d91a1d6a7fa4868e3ed3f67318f09b025942c1f97fd19bb474313c@ec2-3-223-21-106.compute-1.amazonaws.com:5432/daoaaq5b6707cu'
#app.static_folder = 'static'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views